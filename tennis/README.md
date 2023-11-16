# Tennis Refactoring Kata

Imagine you work for a consultancy company, and one of your colleagues has been doing some work for the Tennis Society. Unfortunately he has now fallen ill. He says he has completed the work, and the tests all pass. Your boss has asked you to take over from him. She instructs you to tidy up the code a little and perhaps make some notes so you can give your colleague some feedback on his chosen design.

## Tennis Kata

Tennis has a rather quirky scoring system, and to newcomers it can be a little difficult to keep track of. The tennis society has contracted you to build a scoreboard to display the current score during tennis games. 

Your task is to write a “TennisGame” class containing the logic which outputs the correct score as a string for display on the scoreboard. When a player scores a point, it triggers a method to be called on your class letting you know who scored the point. Later, you will get a call “score()” from the scoreboard asking what it should display. This method should return a string with the current score.

You can read more about Tennis scores [here](http://en.wikipedia.org/wiki/Tennis#Scoring) which is summarized below:

1. A game is won by the first player to have won at least four points in total and at least two points more than the opponent.
2. The running score of each game is described in a manner peculiar to tennis: scores from zero to three points are described as "Love", "Fifteen", "Thirty", and "Forty" respectively.
3. If at least three points have been scored by each player, and the scores are equal, the score is "Deuce".
4. If at least three points have been scored by each side and a player has one more point than his opponent, the score of the game is "Advantage" for the player in the lead.

You need only report the score for the current game. Sets and Matches are out of scope.


# Python Coverage

1. Install the package coverage for python 3
    ```
    pip install coverage
    ```
2. Run the tests with the coverage (will generate the code coverage)
    ```
    coverage run -m unittest test.TestTennis
    ```
3. Generate the report (without details)
    ```
    coverage report -m
    ```
4. Generate the report with html (coverage with details)
    ```
    coverage html
   
   # Check if this directory is there
       ls -rlt htmlcov
   
   # click on htmlcov/index.html to see the coverage on your browser
    ```
 5. If you need to erase the coverage
    ```
    coverage erase
    ```
Did you have 100% coverage? If not, what did we miss and it is important?