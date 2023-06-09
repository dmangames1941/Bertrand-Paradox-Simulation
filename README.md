# Bertrand-Paradox-Simulation

### What is the Bertrand Paradox?
>The Bertrand paradox is a problem within the classical interpretation of probability theory. Joseph Bertrand introduced it in his work Calcul des probabilités (1889), as an example to show that the principle of indifference may not produce definite, well-defined results for probabilities if it is applied uncritically when the domain of possibilities is infinite.
>https://en.wikipedia.org/wiki/Bertrand_paradox_(probability)

### The question preposed:
>The Bertrand paradox is generally presented as follows: Consider an equilateral triangle inscribed in a circle. Suppose a chord of the circle is chosen at random. What is the probability that the chord is longer than a side of the triangle?
In the case of this project to make things easier the circle has a radius of 1 unit making each side of the triangle $\sqrt{3}$ in length.

### The Methods Used:
When Bertrand preposed the question he provided three different ways of calculating a random chord, these methods are the following:
#### The Endpoint Method:
The endpoint method is quite straight forward, you uniformly generate 2 random points on the circumference of the circle and calculate the distance between the two points. As more trials are run with this method, the relative frequency of success tends towards 1/3.
#### The Midpoint Method:
The midpoint method instead of generating 2 random endpoint, this method uniformly generates a random x and y coordinate within the circle. After that it calculates the distance from the center of the circle to the point and the length of the chord and has a success rate of 1/4. For the actual graphing part of the program it continues on by calculating the slope of the chord, and the coordinates of the endpoints.
#### The Random Radial Point Method:
The random radial point method is quite similar to the midpoint method is the sense that it randomly generates a midpoint on a line, however the way it goes about it is different. The random radial point method uniformly generates a point on the radius, r from 0 to 1 and a random angle &theta; from 0 to 2&pi;. From there it applies the conversion from polar to cartesian x = r * cos(&theta;) and y = r * sin(&theta;), followed by calculating the distance from the center of the circle to the point and then the length of the chord and using this method you should have a success rate of around 1/2. Also for plotting purposes it also calculates the endpoints of the line just like in the midpoint method.

*For a better explaination of how each of the methods work: https://youtu.be/mZBwsm6B280*

### My Own Custom Method:
When preposing the project, my Statistics professor asked us to come up with our own method of generating a random chord. Method 4 as I have called it in the program uniformly generates two random points that are not the same point and are contained within the circle. From there it finds the endpoints of the chord that would be generated by those points. This method has a success rate of around 3/4.
