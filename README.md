# Assignment 3 - Replicating a Classic Experiment  
===
Authors: Aditya Patel, Karinne Aiello, Victor Radina
Find the experiment hosted on GitHub Pages [here](https://adityaapatel.github.io/a3-experiment/).

## Experiment Overview
The type of visualization chosen to convey data can have a significant affect on the accuracy of viewers' perceptions. Our team wanted to investigate the idea that stacked bar charts are poor illustrations of information when compared to other charts. To do so, we developed a survey that showed each participant 20 stacked bar, 20 bar, and 20 donut charts and recorded their precision when answering "What percentage is the smaller value of the larger value?" between two shapes marked with bold outline. Each of our ten surveyees viewed their 60 trials with 2 data points marked out of 5 random generations, in random order, and having possible answers between 0% and 100%. When documenting respondents' accuracies between the the true percentage and their reported percentage, we used Cleveland and McGill's equation $\log_2(|judged percent - true percent| + 0.125)$ to avoid the bias that would arise from using `abs(ReportedPercent – TruePercent)` as the score for error. 

## Vises
To rank the three chosen visualization types from best to worst performance, we calculated and reported the average log2Error for each visualization across all trials and participants. See this information in the table below and an example of each visualization type from our survey.

| Visualization Type  | Average Error | Example  |
| ------------- | ------------- | ------------- |
| Bar  | 1.4663  | ![bar](img/Bar_Example.png)  |
| Stacked Bar  | 2.0992  | ![stacked](img/Stacked_Example.png)  |
| Donut  | 2.2203  | ![donut](img/Donut_Example.png)  |

> [!IMPORTANT]
> Given the above collected data from 200 trials for each visualization type, a bar chart is a far better illustrator than a stacked bar or donut chart.

## Intervals


## Achievements
### Technical 
- [x] text

### Design
- [x] text

<!-- BEGIN: Aditya's Contributions -->
## Contributions by Aditya

- Improved code readability by updating all comments in both the HTML (JavaScript) and CSS files.
- Rewrote long, formal comments to be short, clear, and in plain English, making the code easier to understand for everyone.
- Ensured that all code documentation is direct and helpful, following best practices for clarity.
- Helped make the project more accessible for future contributors and reviewers.
<!-- END: Aditya's Contributions -->
<!-- BEGIN: Aditya's Code Explanation -->
## Code Contributions by Aditya

### index.html
- Rewrote and simplified all code comments to be short, clear, and in plain English, making the JavaScript logic easy to follow.
- Used direct section headers (e.g., `// --- STATE ---`, `// --- UI ---`, etc.) to organize the code for readability.
- Updated all helper and rendering function comments to be concise and to the point, so anyone can quickly understand what each function does.
- Example:

```js
// --- HELPERS ---

//vic
// added csv combiners, and log formula - run after all tests are run



// Shuffle arr (Fisher-Yates)
function shuffle(arr) { ... }

// Make 1 trial w/ rand vals, pick 2, calc %
function generateTrial(condition) { ... }

// Arr -> CSV str (w/ header)
function toCSV(rows) { ... }

// DL CSV (makes blob, temp url, auto click, fname w/ PID+date)
function downloadCSV() { ... }
```

### style.css
- Replaced all long or unclear comments with simple, clear English above each CSS block.
- Each section now has a comment that describes its purpose, e.g.:

```css
/* Set font and margin for the page */
body { ... }

/* Limit the container width */
#container { ... }

/* Style for the chart area */
#vis { ... }
```
- This makes the CSS easy to scan and understand for anyone new to the project.
---
<!-- END: Aditya's Code Explanation -->
