Quick Changes
=============
- [ ] Round fractions to 2 decimal places
- [ ] Analyse all markets quickly
- [ ] Can we also parse the time of match?
- [ ] Single wager gives error.
- [ ] Write unit tests for odds_parser
- [ ] Write unit tests for normal_match_parser
- [ ] Write unit tests for odds_analyzer
- [ ] Write unit tests for odds_calculator
- [ ] Write unit tests for main
- [ ] Transform the output recommendations into a CSV file.
- [ ] Be able to run all sports in a single go and generate single CSV for illustration.

Research
========
- [ ] Investigate if instead of scraping, can we use an API that provides us all the data
      for all matches. 
- [ ] Add support for analyzing more than 3 teams 
    - [ ] Add support for dynamic risk profiling
        - [ ] No risk
        - [ ] Least risky option
- [ ] Given odds, calculate wager
- [ ] Analyze and determine the kind of odds that would be profitable. 
- [ ] Can we get upcoming matches information from somewhere?
- [ ] CLI for the tool.

Other Tasks
============
- [ ] Add half time football market to the list
- [ ] Capture Horse Racing Odds
- [ ] Explore python virtual environments - What can we do? 
- [ ] Write functional tests for checking odds. 


Done
====
- [x] Parse odds checker football page, get all the odds and run them through to generate a daily report.
- [x] Add support for adding risk to particular type of odd, example: Percentage of risk tolerance
- [x] Establish a minimum wage
- [x] Create a separate function to generate report, should be moved outside the main method.
- [x] When getting wagers, just get the top 10 wagers, sorted by A, B or C.
- [x] Generate wagers once
- [x] Remove risk allowed from odds
- [x] After running, produce a single summary of recommendations.