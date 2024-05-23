## Data Science Workflow
Data Science is much more than running models, and goes far beyond just reducing and plotting data. Data science is: 
- understanding that how you ask your question determines your outcome
- understanding what you “keep” in data reduction, but also what you discard
- translating a domain problem into an information science problem, then translating the results back again
- understanding why a result or decision was made can be more important than what the result was
- varying your implementations to optimize a solution – faster machines allow you to “fail faster.”
- finding the right tool for the job

### Data Science Lifecycles
Practitioners of data science have studied best practices to maximize the probability of success. Most agree that "business understanding" or "subject matter expertise" is one of the key steps. And, of course, there is data wrangling, which can be expressed in a variety of ways. 

![Data Science Lifecycle diagram, Liu et al. 2021, DOI: 10.1007/978-3-031-01340-9_5, license is Creative Commons Attribution 4.0 International
](/aiml-tutorial/images/Typical-data-science-lifecycle.png)

<!--
<img src="/aiml-tutorial/images/Typical-data-science-lifecycle.png" width="300" alt="Data Science Lifecycle diagram, Liu et al. 2021, DOI: 10.1007/978-3-031-01340-9_5, license is Creative Commons Attribution 4.0 International"/>>
-->

Next comes the process of determining which models to try, and which features work best. This is an iterative process, the simple "circle" is misleading. In reality, there are many iterations, thus there are process models such as the *Cross-industry standard process for data mining*, or **CRISP-DM** that express the need to examine and refine your effort at every stage of the lifecycle. 

![CRISP-DM diagram, Kenneth Jenkins https://commons.wikimedia.org/wiki/File:CRISP-DM_Process_Diagram.png, license is Creative Commons BY-SA 3.0
](/aiml-tutorial/images/crispdm.png)

<!--
<img src="/aiml-tutorial/images/crispdm.png" width="300" alt="CRISP-DM diagram, Kenneth Jenkins https://commons.wikimedia.org/wiki/File:CRISP-DM_Process_Diagram.png, license is Creative Commons BY-SA 3.0"/>>
-->

A team at NASA GSFC studied several ML efforts for science research, and found that even more iterations are typical. For example, dedicating a lot of effort to "data cleaning" is important, but you may not know whether the dataset is sufficient or appropriate until you examine the data more closely and monitor the machine learning model's performance. The following figure documents one specific effort:  

![Generalized science lifecycle diagram, Source: Robert Morgenstern and the NASA Model-Based Approach to Machine Learning Science Task Group
](/aiml-tutorial/images/Generalized_Lifecycle.png)

<!--
<img src="/aiml-tutorial/images/Generalized_Lifecycle.png" alt="Generalized science lifecycle diagram, Source: Robert Morgenstern and the NASA Model-Based Approach to Machine Learning Science Task Group"/>>
-->
### Data Discovery

The JPL Council for *Scientific Understanding from Data
Science*, or *SUDS*, expressed in their Phase 1 Council Report (*Owens et al.*, 2021) how data science and machine learning fit within the landscape of "traditional" science. They found that the traditional "Confirmatory Statistics" approach (e.g. formulate hypothesis, test hypothesis) is augmented by the Data-Driven Approach. This important stage is characterized by Exploratory Statistics and data-driven discovery.  More simply put, it's where you get to know your data, and allow the data to speak for itself. **This may be the most important part of the data science lifecycle, as it creates a pathway to truly new discoveries.**  

It also is an important way to avoid incorrect or misleading results, and it part of the practice of *Responsible and Ethical AI*.

![Scientific Process Diagram, Source: Owens et al., Scientific Understanding from Data Science (SUDS) Council Report, v2.5r CL#21-2945
](/aiml-tutorial/images/suds_diagram.png)

<!--
<img src="/aiml-tutorial/images/suds_diagram.png.png" alt="Scientific Process Diagram, Source: Owens et al., Scientific Understanding from Data Science (SUDS) Council Report, v2.5r CL#21-2945"/>>
-->

### Responsible and Ethical AI

Any time you rely on something to provide you with information, perform an action, or make a decision, you are responsible for the consequences. This is true whether the source is human or a computer. 

A machine learning model will almost always give you an answer, and if you haven't made an error, that answer will be *computationally* correct. However, remember that Data Science is a combination of computation, statistics, and subject matter expertise. The machine learning model cannot produce accurate or useful results if the statistics of the input data set are not appropriate for that task. Additionally, errors can occur if the statistics are robust but they do not accurately reflect the subject domain. For example, most of the scientific data we use requires careful calibration. If the measurements are not correct, then the model could perform perfectly, misleading the user into thinking that the science is also accurate.

AI and Machine Learning (ML) are powerful tools that allow us to analyze and derive knowledge from information that may not be accessible using more traditional methods. AI/ML opens the gateway to exploring more complex relationships in both our data and in our practices as a community of scientists. 
However, the results of any ML model must be examined to ensure that they are valid and beneficial; otherwise the practitioners may act on false or misleading results. 

The best way to fully validate scientific results is to implement explainable and/or interpretable methods. 

**Explainable:**  Generically, an explanation is external.
Commonly a separate model that is supposed to replicate most of the behavior of a black box.

**Interpretable:** Interpretable is inherent in a model.
Constrained in model form so that it is either useful to someone, or obeys structural knowledge of the domain.

For each ML model, there are associated explainable or interpretable methods that can be implemented.  We won't have time to go into this, but <a href="https://docs.google.com/presentation/d/1427_xPaw4LmxzSfo4MdRP3vXhG8ASwEI/edit?usp=drive_link&ouid=113218894171322669312&rtpof=true&sd=true">here is a presentation covering basic principles</a> and some examples. 

**Explainability and interpretability work best when they are integrated with your workflow, expecially when selecting and developing your model.** 

## Common mistakes people make

- Improper splitting of data
- Not examining input and output data closely
- Thinking you told the model to do something when in reality you did something else
- Thinking that the model giving an answer means that it is correct in the statistical or subject matter domains