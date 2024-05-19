# Pioneer-Rocket-Model
Laika Aerospace's project, mid power rocket model. The repository contains openRocket files, simulation and avionics.

# Introduction
Pioneer was created with the idea of building a moderate-capacity launcher capable of testing advanced avionics and recovery systems in unfavorable territory for rocket flight characterized by high apogee. First, Pioneer's payload (FC and camera) hosts a new avionics system, Spike, entirely designed and manufactured by Laika Aerospace. The Flight Computer makes it possible to accurately collect data during flight save and/or send it to the ground. This ensures a pre-flight check of the implemented sensors and constant communications throughout the rocket's flight. The flight computer also allows control of recovery systems (deployment or dual deployment). In addition, Pioneer mounts the new wing and engine block system that can be modulated according to the more or less powerful solid engine configuration. Pioneer will enable future launchers to implement reliable and adequately tested technologies, with the idea of reaching higher apogees and loads. This article discusses the first version and configuration of the rocket, it can however as we will see be modulated to reach Mach 1 and an apogee of 2km.
Pioneer 3d simulation could be find in this repository https://github.com/Deca04/3D-Rocket-Flight-Simulation .

![image](https://github.com/Deca04/Pioneer-Rocket-Model/assets/73656989/07515670-52c6-448d-ba6b-9cf70f638f90)


# The engine Block
Pioneer's engine block, the rocket's solid-fuel engine housing, is one of the new features that our launcher mounts. In fact, the bay is modular, meaning that in combination with different and interchangeable fins it is possible to fit engines with different diameters and lengths without actually rebuilding a new model capable of doing so; the stability is preserved. In order to have sufficient thrust to collect solid data and images of interest, Pioneer is designed to accommodate only engines no smaller than 24 millimeters in diameter and no less than an F/G class according to international classification criteria, even though the model can mount Laika Aerospace-manufactured engines. Rendered images and technical drawings related to housing a 24mm engine follow.
The engine compartment is entirely molded from PLA, and as noted in the picture is closed at the bottom by a truncated cone screwed into the base of the compartment, and at the top sealed by another block with a center hole. The first serves as a block for stable and secure housing, the second as a point of contact for the motor during thrust (morally to prevent the third principle of dynamics from throwing the motor up to the nosecone). Important note, zones of indentation in the press simply allow for savings in weight and overall aerodynamics, as the total mass of the block maintains a center of mass of the rocket corresponding with the rocket's center of gravity, this with or without the fuel mass. Below are precise technical drawings of the upper (1) and lower (2) blocks. 

![image](https://github.com/Deca04/Pioneer-Rocket-Model/assets/73656989/d7d0c8e0-c3d7-4fa7-8f86-bd4693fbc02c)


* Block 1:

![image](https://github.com/Deca04/Pioneer-Rocket-Model/assets/73656989/483aa75c-348e-45ce-b3a3-05964f712eb8) ![image](https://github.com/Deca04/Pioneer-Rocket-Model/assets/73656989/4f05dad8-b1e9-4879-8899-bb85ef393b92)

* Block 2:

![image](https://github.com/Deca04/Pioneer-Rocket-Model/assets/73656989/d56e6fd0-1b00-4d23-8a94-04db0a0a864f)   ![image](https://github.com/Deca04/Pioneer-Rocket-Model/assets/73656989/92d45f85-7b4b-48e4-8237-75f9f223daa7)


   
