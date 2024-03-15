% Define the diet suggestions based on disease
diet_suggestion(cancer, 'Increase intake of fruits and vegetables. Limit processed meats and sugary foods. Drink plenty of water.').
diet_suggestion(diabetes, 'Eat foods with low glycemic index. Monitor carbohydrate intake. Increase consumption of whole grains, fruits, and vegetables. Limit sugary drinks and snacks.').
diet_suggestion(hypertension, 'Reduce sodium intake. Eat a diet rich in fruits, vegetables, and whole grains. Limit alcohol consumption. Avoid processed and fatty foods.').
diet_suggestion(high_cholesterol, 'Choose lean proteins. Increase consumption of fruits, vegetables, and whole grains. Limit saturated and trans fats. Avoid processed foods.').
diet_suggestion(osteoporosis, 'Consume foods rich in calcium and vitamin D, such as dairy products, leafy greens, and fortified foods. Increase intake of foods high in magnesium and potassium. Limit caffeine and alcohol intake.').
diet_suggestion(ibs, 'Identify and avoid trigger foods. Eat smaller, more frequent meals. Increase fiber intake gradually. Drink plenty of water. Limit caffeine and alcohol consumption.').
diet_suggestion(gout, 'Limit purine-rich foods such as red meat, seafood, and organ meats. Increase consumption of low-fat dairy products. Drink plenty of water. Limit alcohol and sugary beverages.').
diet_suggestion(anemia, 'Eat foods rich in iron such as lean meats, poultry, fish, and legumes. Consume vitamin C-rich foods to enhance iron absorption. Avoid drinking tea or coffee with meals.').
diet_suggestion(heart_disease, 'Follow a heart-healthy diet low in saturated and trans fats. Eat more fruits, vegetables, and whole grains. Limit sodium intake. Choose lean proteins.').
diet_suggestion(asthma, 'Consume foods rich in antioxidants such as fruits and vegetables. Limit consumption of processed foods. Avoid foods that may trigger allergic reactions. Maintain a healthy weight.').
diet_suggestion(kidney_stones, 'Stay hydrated by drinking plenty of water. Limit sodium intake. Reduce consumption of oxalate-rich foods such as spinach, nuts, and chocolate. Increase intake of citrate-rich foods like citrus fruits.').
diet_suggestion(pregnancy, 'Eat a balanced diet rich in fruits, vegetables, whole grains, and lean proteins. Consume adequate amounts of folic acid, calcium, and iron. Avoid alcohol, raw fish, and unpasteurized dairy products.').
diet_suggestion(underweight, 'Increase calorie intake by eating nutrient-dense foods such as nuts, seeds, and avocados. Eat frequent small meals. Incorporate protein-rich foods into your diet. Consult a dietitian for personalized advice.').
diet_suggestion(overweight, 'Limit calorie intake by reducing portion sizes and avoiding high-calorie, low-nutrient foods. Increase consumption of fruits, vegetables, and whole grains. Engage in regular physical activity.').
diet_suggestion(_,'No specific diet suggestion available for this disease.').

% Query to get diet suggestion for a specific disease
get_diet_suggestion(Disease, Suggestion) :-
    diet_suggestion(Disease, Suggestion).
/*output
get_diet_suggestion(diabetes, Suggestion).
Suggestion = 'Eat foods with low glycemic index. Monitor carbohydrate intake. Increase consumption of whole grains, fruits, and vegetables. Limit sugary drinks and snacks.'*/
