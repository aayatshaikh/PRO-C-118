import cv2

class BodyClassifier{
  private String bodyType;

  public BodyClassifier(String bodyType) {
    this.bodyType = bodyType;
  }

  public String getBodyType() {
    return this.bodyType;
  }

  public void setBodyType(String bodyType) {
    this.bodyType = bodyType;
  }
}


# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()  

    #Convert Each Frame into Grayscale
    for frame in video:
     frame.convert('L')

    # Pass frame to our body classifier
    body_classifier.process_frame(frame)
    
    # Extract bounding boxes for any bodies identified
    for (BoundingBox) {
    let boundingBox = body.getBoundingBox();
    }

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
