from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        statement_1 = emotion_detector("I am glad this happened")
        self.assertEqual(statement_1['dominant_emotion'], 'joy')

        statement_2 = emotion_detector("I am really mad about this")
        self.assertEqual(statement_2['dominant_emotion'], 'anger')

        statement_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(statement_3['dominant_emotion'], 'disgust')

        statement_4 = emotion_detector("I am so sad about this")
        self.assertEqual(statement_4['dominant_emotion'], 'sadness')

        statement_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(statement_5['dominant_emotion'], 'fear')

unittest.main()
