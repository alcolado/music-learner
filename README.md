# music-learner
Learns to complete music sequences from a given music piece (midi file)

Given an initial midi sequence, it learns to predict what follows (predicted sequence) in the music. 

Here is an example from the second movement of Beethoven's Sonata "Pathetique".
After training for a few hours, it is able to continue sequences of size 50 (of some chosen time unit) almost perfectly

| Initial Sequence ([initial.mid](https://github.com/alcolado/music-learner/blob/master/outputs/initial.mid) )| Predicted Sequence ([prediction.mid](https://github.com/alcolado/music-learner/blob/master/outputs/prediction.mid) ) |
|---|---|
| ![initial](https://github.com/alcolado/music-learner/blob/master/outputs/initial.png) | ![prediction](https://github.com/alcolado/music-learner/blob/master/outputs/prediction.png)|


| Initial Sequence with Target Sequence ([initial_and_target.mid](https://github.com/alcolado/music-learner/blob/master/outputs/initial_and_target.mid) ) | Initial Sequence with Predicted Sequence ([initial_and_prediction.mid](https://github.com/alcolado/music-learner/blob/master/outputs/initial_and_prediction.mid) )|
|---|---|
| ![initial_and_target](https://github.com/alcolado/music-learner/blob/master/outputs/initial_and_target.png) | ![initial_and_prediction](https://github.com/alcolado/music-learner/blob/master/outputs/initial_and_prediction.png)|

