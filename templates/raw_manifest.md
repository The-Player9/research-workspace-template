# Raw data manifest — {{PROJECT_NAME}}

Raw data that is too large to live inside the workspace. Without this file the workspace cannot be traced back to its source after a move between machines.

One block per dataset. Keep it current: an entry added after the fact is usually wrong about the acquisition parameters.

## {{DATASET_NAME}}

- **Location:** {{HOST_OR_NAS}}:{{PATH}}
- **Acquired:** {{YYYY-MM-DD}} by {{WHO_OR_WHICH_SETUP}}
- **Size / extent:** {{SIZE}}, {{NUMBER_OF_FILES_OR_RUNS}}
- **Format:** {{FILE_FORMAT}}
- **Produced by:** {{SCRIPT_OR_INSTRUMENT}}
- **Derived data in this workspace:** `data/derived/{{...}}`, produced by `{{SCRIPT}}`
- **Notes:** calibration, known bad runs, anything that would silently corrupt an analysis
