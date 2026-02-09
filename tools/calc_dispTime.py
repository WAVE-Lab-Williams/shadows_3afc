import pandas as pd
import os

# Read in the data
script_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(script_dir, 'data', 'dataframe_full.csv'))

# Initialize the new column
df['calced_stim_duration'] = None

# Process each participant separately
for pid in df['participant_id'].unique():
    mask = df['participant_id'] == pid
    participant_df = df.loc[mask].sort_values('time_elapsed')

    indices = participant_df.index.tolist()
    categories = participant_df['trial_category'].tolist()
    time_vals = participant_df['time_elapsed'].tolist()

    # Walk through this participant's trials in order
    last_fixation_time = None
    last_calced_duration = None

    for i, (idx, cat, t_elapsed) in enumerate(zip(indices, categories, time_vals)):
        if cat == 'fixationexpt':
            last_fixation_time = t_elapsed
        elif cat == 'dispImageexpt' and last_fixation_time is not None:
            last_calced_duration = t_elapsed - last_fixation_time
            df.at[idx, 'calced_stim_duration'] = last_calced_duration
        elif cat == 'afcexpt' and last_calced_duration is not None:
            df.at[idx, 'calced_stim_duration'] = last_calced_duration
            # Reset after pairing to avoid carrying over to unrelated trials
            last_calced_duration = None

# Save dataframe_full.csv
output_path = os.path.join(script_dir, 'data', 'dataframe_full.csv')
df.to_csv(output_path, index=False)
print(f"Saved to {output_path}")

# --- Update dataframe_answer.csv with calced_stim_duration ---
answer_path = os.path.join(script_dir, 'data', 'dataframe_answer.csv')
df_answer = pd.read_csv(answer_path)

# Build a lookup from the afcexpt rows in dataframe_full: (participant_id, time_elapsed) -> calced_stim_duration
afc_full = df[(df['trial_category'] == 'afcexpt') & (df['calced_stim_duration'].notna())]
lookup = afc_full.set_index(['participant_id', 'time_elapsed'])['calced_stim_duration'].to_dict()

# Match into dataframe_answer by participant_id and time_elapsed
df_answer['calced_stim_duration'] = df_answer.apply(
    lambda row: lookup.get((row['participant_id'], row['time_elapsed'])), axis=1
)

# Round to nearest 100
df_answer['calced_stim_duration_rounded'] = (df_answer['calced_stim_duration'] // 100) * 100
df_answer['calced_stim_duration_rounded'] = df_answer['calced_stim_duration_rounded'].astype('Int64')

df_answer.to_csv(answer_path, index=False)
print(f"Saved to {answer_path}")

# Print a quick summary
populated = df[df['calced_stim_duration'].notna()]
print(f"\nPopulated {len(populated)} rows in dataframe_full.csv with calced_stim_duration:")
print(f"  dispImageexpt rows: {len(populated[populated['trial_category'] == 'dispImageexpt'])}")
print(f"  afcexpt rows: {len(populated[populated['trial_category'] == 'afcexpt'])}")

answer_populated = df_answer[df_answer['calced_stim_duration'].notna()]
print(f"\nPopulated {len(answer_populated)} of {len(df_answer)} rows in dataframe_answer.csv")
print(f"\nSample values from dataframe_answer.csv (ms):")
print(answer_populated[['participant_id', 'time_elapsed', 'calced_stim_duration', 'calced_stim_duration_rounded']].head(10).to_string(index=False))
