import azure.cognitiveservices.speech as speechsdk
import keyboard
import os

class SpeechToTextManager:
    azure_speechconfig = None
    azure_audioconfig = None
    azure_speechrecognizer = None

    def __init__(self):
        try:
            self.azure_speechconfig = speechsdk.SpeechConfig(subscription=os.getenv('AZURE_TTS_KEY'), region=os.getenv('AZURE_TTS_REGION'))
        except TypeError:
            exit("Key not setup error")
        
        self.azure_speechconfig.speech_recognition_language="en-US"
        self.stop_listening_flag = False
    
    def stop_listening(self):
        self.stop_listening_flag = True
        
    def speechtotext_from_mic(self):
        
        self.azure_audioconfig = speechsdk.audio.AudioConfig(use_default_microphone=True)
        self.azure_speechrecognizer = speechsdk.SpeechRecognizer(speech_config=self.azure_speechconfig, audio_config=self.azure_audioconfig)

        print("Speak into your microphone.")
        speech_recognition_result = self.azure_speechrecognizer.recognize_once_async().get()
        text_result = speech_recognition_result.text

        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized: {}".format(speech_recognition_result.text))
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")

        print(f"We got the following text: {text_result}")
        return text_result
    
    def speechtotext_from_mic_continuous(self, stop_key = "p"):
        self.azure_speechrecognizer = speechsdk.SpeechRecognizer(speech_config=self.azure_speechconfig)
        done = False
        final = ""
        # Optional callback to print out whenever a chunk of speech is finished being recognized.
        
        def recognized_cb(evt: speechsdk.SpeechRecognitionEventArgs):
            nonlocal final
            print('RECOGNIZED: {}'.format(evt.result.text))
            final = evt.result.text

        self.azure_speechrecognizer.recognized.connect(recognized_cb)

        # We register this to fire if we get a session_stopped or cancelled event.
        def stop_cb(evt: speechsdk.SessionEventArgs):
            print('CLOSING speech recognition on {}'.format(evt))
            nonlocal done
            done = True

        # Connect callbacks to the events fired by the speech recognizer
        self.azure_speechrecognizer.session_stopped.connect(stop_cb)
        self.azure_speechrecognizer.canceled.connect(stop_cb)

        # This is where we compile the results we receive from the ongoing "Recognized" events
        all_results = []
        def handle_final_result(evt):
            all_results.append(evt.result.text)
        self.azure_speechrecognizer.recognized.connect(handle_final_result)

        result_future = self.azure_speechrecognizer.start_continuous_recognition_async()
        result_future.get()  # wait for voidfuture, so we know engine initialization is done.
        print('Continuous Speech Recognition is now running, say something.')

        while not done:
            # Method to stop recognition when the stop key is pressed
            if keyboard.read_key() == stop_key:
                print("\nEnding azure speech recognition\n")
                self.azure_speechrecognizer.stop_continuous_recognition_async()
                self.stop_listening_flag = False
                break
        final_result = " ".join(all_results).strip()
        print(f"\n\nHeres the result we got!\n\n{final_result}\n\n")
        return final_result