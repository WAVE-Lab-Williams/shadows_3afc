# JSPsych Experiment -- Alternative Forced Choice (AFC)

<!-- Generate a new link for downstream repos using https://deploy-badge.vercel.app/vercel -->
![Vercel Deploy](https://deploy-badge.vercel.app/vercel/experiment-template) 

A user-friendly template for creating online psychology experiments using JSPsych. This template is designed specifically for simple visual perception studies where participants are first presented a singular image, then given several image choices to choose from (to report what they saw)

## What This Template Does

This experiment template:
- Presents one image first, then asks participants to choose from several options what they saw
- Collects response times and which image they reported seeing
- Handles participant consent and demographics
- Works with common research platforms (Prolific, MTurk, SONA)
- Automatically saves all data to WAVE backend system
- Falls back to local data display for testing

## Getting Started

## File Structure Explained

```
shadows_3afc/
├── index.html                    # Main experiment file
├── src/
│   ├── js/
│   │   ├── core/                # Core experiment logic
│   │   │   ├── params.js        # Settings and timing parameters
│   │   │   ├── timeline.js      # Main experiment flow
│   │   │   ├── trial.js         # Single trial logic
│   │   │   └── instructions.js  # All participant-facing text
│   │   ├── utils/               # Utility functions
│   │   │   ├── standard-functions.js
│   │   │   └── plugin-instructions.js
│   │   └── integrations/        # External integrations
│   │       └── wave-client.js   # WAVE backend integration
│   ├── css/
│   │   └── styles.css           # Visual styling
│   └── assets/
│       └── stimuli/             # Image assets
│           ├── circles/         # Circle stimuli
│           └── renders/         # Rendered object/shadow stimuli
├── docs/                        # Documentation
├── tools/                       # Development tools
└── package.json                 # Node.js dependencies
```

## Data Collection

This template uses the WAVE backend system for data collection. **Important**: You must set up your experiment schema in WAVE before collecting data.

📖 **See the [WAVE Integration Guide](docs/setup/wave-integration.md) for complete setup instructions**