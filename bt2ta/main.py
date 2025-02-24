import pyuppaal
from bt2ta.bt2ta import *
import os


# load the leaf node templates
templates_model=pyuppaal.UModel("leaf_node_templates.xml")

# convert the individual leaf node templates into TA helper class
FA=TA(templates_model.templates[0])
print(FA._name)

FB=TA(templates_model.templates[1])
print(FB._name)

FCharger=TA(templates_model.templates[2])
print(FCharger._name)

CBatt=TA(templates_model.templates[3])
print(CBatt._name)

# Be sure to copy the grid and battery TA over too!
Battery=TA(templates_model.templates[4])
Grid=TA(templates_model.templates[5])

##############################################################################
# Here we define the structure of the BT spec and compose the BT automaton
# using the leaf node templates.
##############################################################################

print("Composing BT from leaf nodes")
BT=compose_seq(
    FA,
    compose_seq(
        compose_sel(
            CBatt,
            FCharger
        ),
        FB
    ),
    name="BT",
    params="const int T",
    root=True
)


# remove output file if it exists
if os.path.isfile("BT_converted.xml"):
    os.remove("./BT_converted.xml")

# create new UPPAAL model
model=pyuppaal.UModel.new("BT_converted.xml")

# export the new BT template, battery TA, and grid TA
model.templates=[BT.to_template(), Battery.to_template(), Grid.to_template()]

# add global declarations
model.declaration="""// Place global declarations here.

bool A,B,Charger; // True if robot is in location A, B, or Charger
int Batt;         // Integer variable for the state of charge of the battery
int dt=1;         // Time resolution set to one second
"""

# instantiate system templates
model.system="""// Place template instantiations here.
grid=Grid();
spec=BT(20);
battery=Battery(75);
// List one or more processes to be composed into a system.
system grid, spec, battery;
"""

# add our queries
# these demonstrate that a satisfying trace of the BT exists
# as well as a violating trace (if the mobile robot sits still
# it will violate the BT spec)
model.queries=[
    "E<> spec.Success",
    "E<> spec.Failure"
]

# save the model
# it can now be opened in UPPAAL!
model.save()
