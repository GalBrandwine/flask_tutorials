from utils.camera import VideoCamera
import cv2


class TestVideoCamera:

    def test_get_frame(self):
        """Test if camera captures video. """

        # setup
        camera = VideoCamera()
        print("test")
        # run
        while True:
            frame_returned = camera.get_frame()
            success, frame_decoded = cv2.imdecode(frame_returned, 1)
            cv2.imshow("Decoded", frame_decoded)
            k = cv2.waitKey(0)
            if k == 27:  # wait for ESC key to exit
                cv2.destroyAllWindows()
            assert success is True
