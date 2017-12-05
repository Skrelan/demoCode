# My solution
## Environment info:
* Python 2.7
* MAC OS X 10.11.2

## Running the script:
open terminal and run `python app.py`

## Code distribution:
The code sits in the following files:
* app.py
* logic.py
* utils/utils.py
* models/models.py

### app.py :
This is the main worker / abstract layer

### logic.py :
All the logic dealing directly with the data sits here:
* read_demographic() : reads the demo.psv file and collects demographic Data
* read_events() : reads the events.psv file and only stores records that has valid demographic data.
* clean_up() : cleans up `store` of patient_ids that do not have any events
* stats() : iterates through the `store` dict and collects stats
* write_to_file() : writes the contents of `store` dict into a local JSON file postfixed with a time-stamp in the output directory

### utils/utils.py :
This contains all the utility/helper functions that are used by logic.py

### models/models.py :
This is used to define classes which help with defining a structure and storage of all the data.
