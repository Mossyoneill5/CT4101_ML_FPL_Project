# Evaluation Plan
This plan sets out how the models will be evaluated.

## Prediction context 

This project estimates each players total FPL points for the 2025-26 season using their statistics and profile information from the same season. It is a supervised regression problem. It covers premier league players who played at least one minute in the season. Because the estimate is made at the end of the season all features are available at prediction time. This is a model of the season played and it is not a forecast of how many points a player will earn in a future season.

## Candidate Features and rationale 

The following are selected as candidate features based on data audit and domain knowledge:
- **minutes**: players need time on the pitch to score points.
- **starts**: starting players usually play more minutes and earn more points.
- **now_cost**: price indicates quality of the player.
- **position**: points rules differ for each position.
- **team**: players in stronger teams get more goals.
- **selected_by_percent**: shows how many managers picked the player.
- **cost_change_start**: price changes reflect how the player has performed during the season.

**Target:** total_points, the total FPL points earned by each player during the 2025–26 season.

Two following two features are engineered from existing columns.They are not included in the baseline which is kept simple and can be tested in later milestone.

- **age**: a players age may relate to how well a player earns points.  Very young or older players may not perform as well. It is available at prediction time.
- **transfer_balance**:  the difference in transfers_in and transfers_out. This can indicate whether managers are buying or selling a player. Available at prediction time. 

## Test strategy

20% of the players are held back as a test set. A random split is used with random_state=42 for the train/test split, the cross-validation folds and any model with randomness, so every run gives the same results.

**Unit of analysis:** Because each row is a separate player there is no duplicate player. Each player appears only once so the same player cannot be in both the training and test data.  

Players belong to one of 20 teams. Team is used as a feature so players from the same team can appear in both training and test sets. This is not leakage because the model predicts individual players not teams. 

The data is a single snapshot taken at the end of the season. There is no time order between the rows so a random split will work here. 

## Preprocessing 

Any missing numerical features are filled with the median and then scaled with StandardScaler. 
Nominal features like position and team, missing values are filled in with the most frequent value and one hot encoded. The audit found no missing values in the selected features so imputation will not change any value in the current data.
All steps are run inside a pipeline fitted on the training data only. During cross-validation the pipeline is fitted again inside each fold.  So this means the validation fold is not used to calculate the median, scaling or encoding. 

## Cross-validation

Models use 5-fold cross-validation on the training data. (KFold, shuffled,random_state=42).
Five folds gives a good estimate with about 86 players tested per fold from 429.
Because players are independent and there is no time order in the data KFold is appropriate. Group or time splitter would only be needed. 

## Baselines

- **DummyRegressor**  is the baseline model that predicts the mean total points from the training data for each player. Any good model should perform better than this. 

- **LinearRegression** is the simple learned baseline. It uses the same features, preprocessing pipeline and cross-validation as the dummy. 

## Metrics 

The primary metric is MAE. This measures on average how far the models predicted points are from the actual points.
The secondary metrics are RMSE and R².
RMSE weights large errors more heavily so it highlights when the model makes big mistakes. 
R² is an overall measure of how much better the models predictions are than predicting the average points. 

## Regression error 

Predicting too high or too low is equally bad for this project. MAE treats both types of error the same so is the main metric chosen. 

## Leakage Register 

- **Target leakage** — columns that directly contribute to total points (goals, assists, bonus, etc.) are left out of the candidate features.  However minutes played is retained because it is an important measure of playing time, even though it also contributes to total points.  selected_by_percent and cost_change_start indirectly relate to the points as managers select players who are scoring points and prices rise as a result. They are kept because they are available at prediction time but this is a limitation.

- **Train test contamination** — Imputation, scaling and encoding are performed within a pipeline with only the training data. This prevents information from the test set being used during training. Features were chosen from the data audit using domain knowledge before any modelling was done. They were not selected using model scores or the test set.

- **Group / temporal leakage** — Each player appears only once in the dataset, so there are no repeated player records across the training and test sets. A random split is used because the dataset contains one record per player and as there is no time order in the data a random split is suitable. 

- **Limitations** - Some features including minutes played, matches started and current player prices contain information collected during the season. This project investigates whether total points for the 2025–26 season can be estimated using player profile features collected during the season rather than predicting points before the season begins. These features would not all be suitable for pre season predictions because some of this information would not yet be available. 

## Final test set access
The 20% test set is kept separate during model development and is only used at the end to evaluate the final models performance. It is not used for selecting models or tuning their settings.