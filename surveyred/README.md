# sample-survey-design
Please open the index.html to understand the flow of this sample website.

Segment 1: There you will find three variable in <script> tag. 
		1) survey_intro 
		2) survey_sample_page 
		3) survey_finish
These three variables are the definition of each page of the survey.

Segment 2: `jsPsych.init` is the initialization of the page. Here `timeline` object will contain the variable declared earlier. The sequence of these in variables should be in the way which you want participants to watch. `on_finish` object will contain a js function which will derive at the end of survey what actions will be taken or done. 

Segment 3: `jsPsych.data` is the variable through which we will be able to get all the information provided by participants during experiment. 
 
