# A Novel CAMPD Methodology for Optimizing Working Fluids Design in Organic Rankine Cycles for Waste Heat Valorization

This repository includes the data and models developed to ensure the reproducibility of the results presented in the paper.

The generated molecular structures are provided in SMILES format within the Excel file named "Candidates". Major optimization results for both the dual ORC and the OFRC configurations, using the set of 35 well-established working fluids, are also provided in excel files "Results_ODRC" and "Results_OFRC". Antoine coefficients for these fluids are also shared in "Antoine_coefficients" excel file.
The predictive model for GWP estimation is distributed across two files: a .joblib file, which contains the trained model, and a .joblibparameters file, which specifies the molecular descriptors required to apply the model.
The model for predicting the flammability class (FC) is saved as a .keras file. To use this model, it is necessary to first run the "features_flammability" script, which transforms the SMILES strings into the input features needed for FC prediction. These features include molecular composition parameters (the number of C, H, F, Cl, Br, I, O, and N atoms), the presence of double bonds, the molecular mass, and the HR index.
The GCN models for net power and upper pressure of both cycles are stored as .tar.

