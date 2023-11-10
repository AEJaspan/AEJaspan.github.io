<!-- https://www.dkgrdatasystems.com/portfolio/robotic-inspection -->

# Robotic Inspection Project

This project represents a significant advancement in bridge inspection, utilizing robotics and computer vision to analyze cable defects on stay-cable bridges. Initially, the challenge was to make the images captured by an inspection robot both useful and usable.

A drone-based solution was initially considered but found unsuitable due to the precision required in analyzing cable defects. As an alternative, a robotic system was developed. This system featured a ring of cameras, each capturing images along the cable. I then developed a method of stitching these images together to form a cohesive view of the cable's condition.

My focus in this project was the software development. In doing so, I successfully implemented several key functionalities:

1. **Distortion Correction:** Before stitching, the images were corrected for any distortions.
2. **Automated Stitching:** The software stitched image tiles around and along the cable.
3. **Defect Detection:** Computer vision was employed to automatically detect cable defects.
4. **Interactive User Interface:** A user interface was developed using React, running locally via Electron. This interface interacted with a backend Python server for image analysis, allowing users to view large composite images, identify detected defects, and add manual annotations.
5. **High-Resolution Imaging:** The interface was capable of displaying very large images at deep zoom levels, a feature tested with ultra-high-resolution images from the Hubble Space Telescope.
6. **PDF Report Generation:** The system could automatically generate PDF reports from the images and annotations.

A core component of this project was the utilization of modern computer vision techniques to detect and localize defects on the cable surface. This utility of the product makes it possible for on site engineers to quickly assess large quantities of image data, with their attention being effectively focused on sites with the most probable signs of damage.

![Object detection and localisation](/assets/img/posts/automateddetection.jpg)

An early prototype of the cable viewer front end can be seen below. This displayed test images from a cable, facilitating user annotations. It's worth noting that this prototype used placeholder data from the Anzac Bridge for demonstration.

![Annotations provided in the frontend](/assets/img/posts/annotations.jpg)

The project's success hinged on adopting an agile approach, which enabled continuous development and integration of new features as additional data from the robot became available. This approach ensured the delivery of working software throughout the project’s lifecycle.

This project was a blend of research (for automated defect detection) and solid software engineering. Close engagement with the client ensured the final product was tailored to their requirements, successfully transforming a series of proofs-of-concept into a cohesive, functional product.