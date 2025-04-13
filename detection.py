import cv2

def detect_ppe(model, frame):
    """
    Detect PPE equipment in the given frame using the YOLO model
    
    Args:
        model: YOLO model instance
        frame: Input image/frame (BGR format)
        
    Returns:
        output_frame: Annotated frame with detections
        missing: List of missing PPE items
        item_counts: Dictionary of detected items and their counts
    """
    # Resize frame for faster processing (optional)
    frame = cv2.resize(frame, (640, 640))
    
    results = model.predict(frame)
    output_frame = results[0].plot()
    
    detected_classes = []
    for result in results:
        classes = result.boxes.cls.cpu().numpy()
        detected_classes = [model.names[int(cls)] for cls in classes]
    
    # Count each detected item
    item_counts = {}
    for item in detected_classes:
        item_counts[item] = item_counts.get(item, 0) + 1
    
    required_ppe = ["helmet", "vest", "gloves", "boots"]
    missing = [item for item in required_ppe if item not in item_counts]
    
    return output_frame, missing, item_counts