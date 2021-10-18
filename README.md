
# CodingPuzzles
Coding Puzzles with Solutions
## 1. Conference Event Planner
  The constraints are as follows:
  1.	The event has a morning and an afternoon session.
  2.	Each session contains multiple talks.
  3.	We also have Poster Presentations and Networking Event at the end of the day (4pm to 6pm)
  4.	Morning Session begins at 8 am and must finish by 12 noon, for lunch.
  5.	Afternoon Session begins at 1pm and must finish in time for Poster Presentations and Networking Event.
  6.	Not talk has been ordered. 
      a.  Each talk has a duration in minutes or they will be Vignettes which are 5 minutes long.
      b.	All the talks will be from our Home Experts.
      c.	All the Expert talks should be scheduled between 8 am and 4pm. Just in time for “The Poster Session and Networking Event”
          i.	Since we have a lot of papers, we will have multiple tracks for Paper presentation 
      d.	Presenters will be very punctual. There needs to be no gap between Sessions.
  7.	Plan for two 15 minute breaks:
      a.	One in the morning session from 10:45 to 11:00 am
      b.	One in the afternoon session from 2:30 pm to 2:45 pm

### Test Input:
  EUV Catch me if you Can (Home Expert) 30 min  
  Wonder Defects and Where to find them? (Home Expert) 75 min  
  Architecting the Intelligent Apps Engineer (Vignette)  
  Quantum Entangled Inspection (Home Expert) 70 min  
  Tesla’s Legacy (Vignette)  
  Quantum Revolution by Super Clean Reticles (Home Expert) 60 min  
  Q#ing to Entropy Modeling (Home Expert) 45 min  
  Geek’s Life (Vignette)  
  BBP – Speed I am Speed (Home Expert) 45 min  
  What is a bug? – Test Driving to a Bug Free Universe (Home Expert) 90 min  
  Git your Rational Team Concert out of here (Home Expert) 35 min  
  Future of Particle Imaging with Muons (Vignette)  
  Continuous Delivery in a Disconnected Environment (Home Expert) 85 min  
  Atomic Transistors -> Super Computing in your Palm (5 min)  
  eBeam Wafer Inspection – Saves the Day (Home Expert) 60 min  
  Up for a real challenge - beyond the world of Mobile Apps (Vignette)  
  What if Tesla was lucky enough to work for us? (Vignette)  
  Quantum Revolution by Super Clean Reticles (Home Expert) 25 min  
  Quantum Machine Learning (Home Expert) 60 min  
  Defect Location Accuracy at the Atomic Level (Home Expert) 60 min  
  Timing the Photon Pulse (Vignette)  

### Test Output:
  #### Track 1:
  08:00 AM eBeam Wafer Inspection – Saves the Day (Home Expert) 60 min  
  09:00 AM BBP – Speed I am Speed (Home Expert) 45 min  
  09:45 AM EUV Catch me if you Can (Home Expert) 30 min  
  10:15 AM Quantum Revolution by Super Clean Reticles (Home Expert) 25 min  
  10:40 AM Geek’s Life (Vignette)  
  10:45 AM Break (15 min)  
  11:00 AM Quantum Machine Learning (Home Expert) 60 min  
  12:00 Noon Lunch 60 min  
  01:00 PM What is a bug? – Test Driving to a Bug Free Universe (Home Expert) 90 min  
  02:30 PM Break (15 min)  
  02:45 PM Tesla’s Legacy (Vignette)  
  02:50 PM Quantum Entangled Inspection (Home Expert) 70 min  
  04:00 PM Poster Session and Networking Event (120 min)  

  #### Track 2:
  08:00 AM Q#ing to Entropy Modeling (Home Expert) 45 min  
  08:45 AM Wonder Defects and Where to find them? (Home Expert) 75 min  
  10:00 AM Git your Rational Team Concert out of here (Home Expert) 35 min  
  10:35 AM Up for a real challenge - beyond the world of Mobile Apps (Vignette)  
  10:40 AM What if Tesla was lucky enough to work for us? (Vignette) 
  10:45 AM Break (15 min)  
  11:00 AM Quantum Revolution by Super Clean Reticles (Home Expert) 60 min    
  12:00 Noon Lunch 60 min  
  01:00 PM Continuous Delivery in a Disconnected Environment (Home Expert) 85 min  
  02:25 PM Atomic Transistors -> Super Computing in your Palm (5 min)  
  02:30 PM Break (15 min)  
  02:45 PM Defect Location Accuracy at the Atomic Level (Home Expert) 60 min  
  03:45 PM Timing the Photon Pulse (Vignette)  
  03:50 PM Future of Particle Imaging with Muons (Vignette)  
  03:55 PM Architecting the Intelligent Apps Engineer (Vignette)  
  04:00 PM Poster Session and Networking Event (120 min)  
  
## 2. FizzBuzz Problem - Library and Console Application
  For each multiple of 3, print "Fizz" instead of the number  
  For each multiple of 5, print "Buzz" instead of the number  
  For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number  

## 3. Leet Code Problems
  Solutions to Some of the Leet Code Problems
