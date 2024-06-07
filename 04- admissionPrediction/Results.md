# Assignment 4: Analysis of Dataset to Determine Chance of Admission from Parameters of Academic Excellence

## Libaries Used
1. `numpy`: Taking Input from CSV File, Calculating Functional values for an array of parameter values
2. `scipy`:`scipy.optimize.curve_fit` was used to optimise the parameters for the solution models proposed

## Approach
I used two models to predict the Chance of Admission for the given parameters: A linear model and a model with arbitrary power for each of the parameters. This gave decently good approximates and using other models such as those involving exponentials did not yield considerably better results.

The parameters were normalised to have a maximum value of 1 (all the parameters were divided by the maximum attainable value of the same). This was done to ensure that the coefficients obtained can be used to describe the trends of the chance of admission quantitatively easier.

The parameters in consideration are namely: GRE Score, TOEFL Score, University Rating, SOP, LOR , CGPA and Research

## Linear Model
The chance of Admission was assumed to be a linear function of all the parameters. Then, `curve_fit` was used to optimize the coefficients of all the parameters. This was done because this seemed the simplest model for this data. Also, plotting the graph between most of the parameters  and the chance of admission is close to linear(everything seems closely distributed wrt a line, with a few points far from it).

The average relative error was found to be **6.8537%**.

The solutions obtained was:
($x_{0}$,$x_{1}$,$x_{2}$....$x_{6}$ are the normalised values of the parameters GRE Score, TOEFL Score, University Rating, SOP, LOR , CGPA and Research respectively)

$0.631892x_{0} +0.33335666x_{1} +0.02970688x_{2} +0.00793064x_{3} +0.08429374x_{4} +1.1838506x_{5} +0.01215374x_{6} -1.2635712$

- This indicates the highest dependence of the chance of getting in on CGPA, followed by GRE Score, TOEFL Score, LOR and other parameters.
- Also, choosing research has a greater chance of acceptance, as seen from the fact that its coefficient is positive
- However, the relationship between university ranking is quite counterintuitive, as it is positive. It makes sense for the chance to decrease with the university getting better.
- Coefficients of all the parameters are positive, implying that they add to the chances of admission.

## Non-Linear Model
The solution was assumed to be a linear combination of all parameters raised to different parameters. This was done to obtain a better fit than the previous one. And it did, with an average relative error of **6.8336%**.

The solution obtained is given below(the variables are in the same order as before):

$3.0706\times10^{1}x_{0}^{{1.955\times10^{-2}}} +4.0687\times10^{1}x_{1}^{7.927\times10^{-3}} -5.8746\times10^{1}x_{2}^{-1.039\times10^{-4}} +2.3114\times10^{-2}x_{3}^{1.066\times10^{1}}  +7.8147\times10^{-2}x_{4}^{1.132\times10^{0}}+4.5172\times10^{1}x_{5}^{2.218\times10^{-2}} +1.2749\times10^{-2}x_{6} -5.6916\times10^{1}$

- University Ranking has a negative coefficient and a small negative exponent. This is pretty counterintuitive as well because it says that when the university rating increases, the chance of admission increases as well. This is not necessarily true in real life.

- The next set of strong dependences are in TOEFL, CGPA and GRE Scores in decreasing order of dependency. They have positive coefficients and small positive exponents. 

- All the other parameters have a positive dependency with chance of admission, that is, as the parameters increase, the chance of admission increases.

- The coefficient of research is positive, indicating that people choosing research have higher chance of admission.

## Conclusions
1. GRE, TOEFL and CGPA have a strong dependance on chance of admission. They are the parameters to be maximized to increase one's chances of admission. Of these parameters, according to the Non-Linear Model, one has to maximise TOEFL Score and according to the Linear Model, one has to maximise CGPA

2. It is quite counterintuitive that the better the rating of university increases one's chances of admission.

3. People choosing research have a higher chance of getting admitted to a college than those who do not.

4. All the parameters given increase chances of admission.