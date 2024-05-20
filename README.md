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
2. Lets do howSum. canSum & howSum has same time complexity before memoized which is O(n^m) (m = target, n = arr.length()). I actually don't know if my code on canSum is O(n^m _ m) because my return doesnt really copy the thingies but just appending new thing to the ans before. so yeah i dont think its O(n^m _ m) CMIIW.
