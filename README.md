# MotorImagery-BCI

In this project, a 5-class Motor Imagery Brain-Computer Interface was developed to actuate the [Freenove Robot Dog](https://store.freenove.com/products/fnk0050).

**Redmine Report:** https://redmine.fe.up.pt/projects/osb-i-onitos-bci/wiki

**Use case diagram:**

![usecase](https://github.com/user-attachments/assets/e2149907-355d-4aae-a5c3-3e1107fbff91)

**EEG Analysis:** The methodology used follows the Frequency Bank Common Spatial Patterns (FBCSP) algorithm in which 17 frequency bands were filtered from the original signal (4-8Hz, 6-10Hz, 8-12Hz, ..., 36-40Hz). Posteriorly, the CSP method was hard-coded (no library was used) following its mathematical equations to extract the oscillatory features in each frequency band. Finally, the Mutual-Based Information method was implemented to select the 4 most discriminative frequency band data comprising the neural activity related to the imagined movements here elicited specifically for each subject. The classification stage was handled in a One Versus the Rest (OVR) manner where the best classifier (LDA vs SVM) was used and optimized to actuate the robot. An 80/20 sing-trial trial split in a 10-fold Cross-Validation loop were used.

The algorithm was initially validated using a [109-participant Online Motor-Imagery EEG dataset](https://physionet.org/content/eegmmidb/1.0.0/) before being applied and tested with our own EEG recording (1 participant). Because BCI models, especially Motor-Imagery paradigms, are subject-specific, one participant is enough to evaluate the robustness of the methodology.

**Acquired channels:** FC5, FC1, FCz, FC2, FC6, C5, C3, C1, Cz, C2, C4, C6, CP5, CP1, CP2, CP6 

**The 5 EEG classes recorded are:**

1 - Lack of movements

2 - Left hand (LH)

3 - Right hand (RH)

4 - Both hands (BH)

5 - Both feet (BF)

In order to expand the robot's mobility options, 2 different movement paradigms are activated depending on the robot's Ultrasonic proximity sensor input, essentially producing 9 different movements with 5 EEG classes.

If the proximity sensor detects an object 5 cm away for more than 1 second the imagined movement classes represent the following robot movements:

1 - Rest

2 - Left Turn (LH)

3 - Right Turn (RH)

4 - Robot Stands (BH)

5 - Robot Sits (BF)

Otherwise (Default movement paradigm):

1 - Rest

2 - Forward movement (LF)

3 - Backwards movement (RH)

4 - Robot legs extend (BH)

5 - Robot lowers itself (BF)

**Results from acquired EEG:**

The classifiers' training comprised 67 imagined movement trials per class while 17 trials (also per class) were used in the testing phase. The classifier bar plots compare the BCI performance according to the number of CSP components used to train and test the models. 

Training results:

![TrainClass_cp](https://github.com/user-attachments/assets/18230128-3370-4a43-8adb-59a34a34524d)

Testing results:

![TesteClass_cp](https://github.com/user-attachments/assets/ca00b135-6e36-4949-b4fa-9b1f84afd3dc)

Most discriminative frequency bands:

![alltraindata_n_bands](https://github.com/user-attachments/assets/7a0c97af-2cde-4ac5-8736-b090443dac9b)


