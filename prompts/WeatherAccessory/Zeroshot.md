# Zero shot prompts for weather accessory environment

## Test Case 1

### Answer

Accessory: Sunscreen
Clothing: Warm

### Prompt
Consider the following data about weather conditions for the last 7 days:

- Temperatures (in °F): [47.348949541566256, -31.622330311862147, 25.32772017492796, -41.84648929886844, 13.360171709887624, 4.580407868630644, 60.09024980191904]
- Weather Conditions: ['Sunny', 'Sunny', 'Sunny', 'Snow', 'Snow', 'Sunny', 'Rain']

Based on the above data, what should be the ideal accessory (Sunscreen, Umbrella, Snowshows) and clothing (Warm, Medium, Summer) choice? Please explain your reasoning.

## Test Case 2

### Answer

Accesory: Snow Boots
Clothing: Warm

Consider the following data about weather conditions for the last 7 days:

- Temperatures (in °F): [22.83072037402046, -5.943323548806106, 18.04667056770205, -3.458765519049905, -19.762368035884755, 36.123639166518316, 0.1366724597284943]
- Weather Conditions: ['Snow', 'Snow', 'Snow', 'Snow', 'Snow', 'Sunny', 'Snow']

Based on the above data, what should be the ideal accessory (Sunscreen, Umbrella, Snowshows) and clothing (Warm, Medium, Summer) choice? Please explain your reasoning.

## Test Case 3


### Answer
Accessory: Sunscreen
Clothing: Medium

Consider the following data about weather conditions for the last 7 days:

- Temperatures (in °F): [11.002115736259952, 25.77717989852053, 45.70660154559317, -1.4454765067394746, 4.221416299114523, 88.05696430588628, 61.881709123364345]
- Weather Conditions: ['Sunny', 'Sunny', 'Sunny', 'Snow', 'Snow', 'Sunny', 'Sunny']

Based on the above data, what should be the ideal accessory (Sunscreen, Umbrella, Snowshows) and clothing (Warm, Medium, Summer) choice? Please explain your reasoning.

## Test Case 4

### Answer

Accessory: Umbrella
Clothing: Medium


Consider the following data about weather conditions for the last 7 days:

- Temperatures (in °F): [9.287147267510534, 73.48475509951476, 87.66865782728809, 15.196600323104775, 112.17624199936816, 83.48090999925077, -42.886762636034206]
- Weather Conditions: ['Snow', 'Sunny', 'Rain', 'Snow', 'Rain', 'Rain', 'Sunny']

Based on the above data, what should be the ideal accessory (Sunscreen, Umbrella, Snowshows) and clothing (Warm, Medium, Summer) choice? Please explain your reasoning.

## Test Case 5

### Answer

Accessory: Umbrella
Clothes: Summer

### Prompt

Consider the following data about weather conditions for the last 7 days:

- Temperatures (in °F): [41.98912734745139, 76.41813000021108, 100.08244386620807, 98.8189150803761, 62.20653504258892, 66.98685226289354, 107.33065166168099]
- Weather Conditions: ['Rain', 'Rain', 'Rain', 'Rain', 'Rain', 'Rain', 'Rain']

Based on the above data, what should be the ideal accessory (Sunscreen, Umbrella, Snowshows) and clothing (Warm, Medium, Summer) choice? Please explain your reasoning.