from rdkit import Chem
import numpy as np
from tensorflow.keras.models import load_model
from mordred import Calculator, descriptors
from rdkit import Chem
from sklearn.preprocessing import StandardScaler
import joblib
def extract_features_from_smiles(smiles):
    
    clean_list_of_smiles = [smi for smi in smiles if Chem.MolFromSmiles(smi,sanitize=False) != None]
    molecules = [Chem.MolFromSmiles(i) for i in clean_list_of_smiles]
    features = []
    atom_counts = {element: 0 for element in ['C', 'H', 'F', 'Cl', 'O', 'N', 'Br', 'I']}
    for molecule in molecules:
        atom_counts = {element: 0 for element in ['C', 'H', 'F', 'Cl', 'O', 'N', 'Br', 'I']}
        for atom in molecule.GetAtoms():
            element = atom.GetSymbol()
            if element in atom_counts:
                atom_counts[element] += 1

        mol_weight = Chem.Descriptors.MolWt(molecule)

        double_bonds = sum(1 for bond in molecule.GetBonds() if bond.GetBondTypeAsDouble() == 2)

        hydrogen_count=sum(atom.GetTotalNumHs() for atom in molecule.GetAtoms())
        
        # Ajustar el conteo de hidrógenos
        atom_counts['H'] = hydrogen_count
        H_count = atom_counts['H']
        HR = (H_count * 1.008) / mol_weight if mol_weight != 0 else 0  # 1.008 es el peso atómico del H


        features.append([
            atom_counts['C'],  
            atom_counts['H'],  
            atom_counts['F'],  
            atom_counts['Cl'], 
            atom_counts['O'],  
            atom_counts['N'],  
            atom_counts['Br'],  
            atom_counts['I'],   
            HR,                 
            double_bonds,       
            mol_weight          
        ])

    return np.array(features)

