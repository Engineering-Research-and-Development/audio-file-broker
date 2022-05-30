# Audio File Broker


## Table of Contents

-   [Intro](#intro)
-   [Dockerized Repository](#docker)
-   [Requirements and installation](#requirements-and-installation)
-   [Server](#server)
-   [Client](#client)
-   [Roadmap](#roadmap)
-   [License](#license)
-   [References](#references)



## Intro

The Audio File Broker component is an input module for solutions involving audio processing. It was born as input node for the Akimech pipeline in the AI Regio project, involving several cooperating modules for the speech-to-text and topic recognition tasks with the aim of supporting industries in the maintenance processes. 

![immagine](https://user-images.githubusercontent.com/103200695/170997379-f82d335d-62ca-4978-aac2-c85a5712de8c.png)

This component is made of two sub-systems:
- A HTTP server receiving data
- A GRPC server putting data into the pipeline


Moreover, the additional microphone client tool is provided in this repository to allow the use of input audio from a microphone
