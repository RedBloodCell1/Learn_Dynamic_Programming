Today i will learn dynamic programming from this youtube video

## Dynamic Programming - Learn to Solve Algorithmic Problems & Coding Challenges

https://youtu.be/oBt53YbR9Kk?si=LX6iArg8XaO_Quvz

Day 1:

- Today i will learn about dynamic programming

What i learn today:

1. Memoization = hashmap, dictionary in python. Simply mapping what we have get before to the map as a key pair value so the recursion doesn't need to run if the key is already there. really simple. Good way of doing DP:
   - Draw the problem (as a tree) and try to understand the problem
   - Find the base case by trying really small case
   - Make the code work for small number
   - Memoization (Store return value to memo / map) and then return the memo
2. Solve fibonacci problem = O(2^n) -> O(n) time complexity // O(n) space complexity
3. Time complexity:
   - O(n) time is simply it runs n number of time // O(n) space is how much space it took from the problem, at one time
   - But lets not forget that any multiplicative values can be removed as it doesnt matter that much EX: O(n/2) -> O(n)
4. Solve Grid traveler problem = O(2^n+m) -> O(m x n)

5. I will try to do the next problem by myself. Wish me luck (canSum). UPDATE: IDK WHY, MY CODE IS THE SAME BUT PRODUCE DIFFERENT RESULT. PLS HELP ME... OKAY I KNOW WHY IT BREAK. IT IS BECAUSE THE THINGIES IS NOT FLUSHED PROPERLY. IM REALLY ANGRY IDK, idk why when i print new thingies, it decided to keep the map from the iteration before which break my code. idk why this happen but it is supposedly to make a totally new map whenever i call the function again. man idk

Day 2:

Instead of saying what i learn today, i should say, what is in my thought today:

1. New day fresh brain? I dont think so, i just did some cardio so im pretty tired, but im bored (Im detoxing again xdd). So lets do 2 part of DP and call it a day (its 22:55 rn). Im still bothered by the map that is not flushed properly
2. Lets do howSum. canSum & howSum has same time complexity before memoized which is O(n^m) (m = target, n = arr.length()). I actually don't know if the complexity of my code on howSum is O(n*m^2) because my return doesnt really copy the thingies but just appending new thing to the ans before. so yeah i dont think its O(n*m^2) CMIIW.

Day 3:

So whats on my brain today?

1. New day, its 12:10 right now, well i know its not morning anymore, well im learning about kmp algorithm, my brain hurts. im learning lpm (longest prefix m(?)). I watch the video like 4 times or 5 times idk, i still don't understand fully about what its talking about, but i sure understand something. Well it took me like 45 minute until this point. Well lets start our lesson today.
2. Talking about howSum again, what i realize is, i don't really understand time and space complexity. I think i need to work on this a bit more. Because my code is quite different than one in the video, i don't think its the same for time and space complexity. In my map, what i think about is only how the map need to only mapped nothing? What???

This is my process of thought. So his code is actually memoizing the target sum which i dont think is needed??? Because once you found one, u just need to return the first one, so if its done then its done so dont need to memoize anything. Then

- I only memoize the incorrect target number for example 7,[3,5,6]
- It will go to 4 to 1 to -2, then it return none
- It will go to -4, then it also return none
- It will go to -5, then it also return none
- Continue to the below for loop, now it maps that 1 is literally an impossible number to reach.
- Now back to the 4, iteration for target=1 is already none
- Now it will go from 4 to -1 which return none
- Then it will go from 4 to -2 which return none
- Then it maps that 4 is literally and impossible number to reach.
- When the iteration reach 7-6 which produce 1. We dont need to go even further because we know that 1 is impossible to reach. So thats it about my code

So what do i find in this? The space complexity is literally just O(n) ps: target = m, because it will keep the map for each number that is not possible to reach in which the maximum case of it is actually just O(m/2) which will translate to O(m). Why O(m/2) you might ask? Because if there is a 1 inside the list, the its simply just done right? But there might be a 2 inside the list with the target being and odd number. Thats why i get O(m/2). PLEASE CMIIW BECAUSE THIS IS JUST ME TALKING TO MYSELF.

For the time complexity, i don't really understand, but what i know is, it will cut off every single iteration that is not possible to reach, and my code doesn't really copy things, so i guess my code time complexity is O(n\*m) because for each........ I DONt uNDERSTAND YET. Sorry lets just continue then

3. Lets continue to bestSum. I will eat first, cya later probably or next day.

Day 4:

So what is inside my brain today:

1. Lets not waste time and just continue. Same as always, i will try to code by myself first, if im stuck then ill go for the solution, as simple as that
