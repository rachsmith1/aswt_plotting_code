from coffea.nanoevents.schemas.base import BaseSchema, zip_forms
from coffea.nanoevents.methods import base, vector

class NtupleSchema(BaseSchema):
    def __init__(self, base_form):
        super().__init__(base_form)
        self._form["contents"] = self._build_collections(self._form["contents"])
        
    def _build_collections(self, branch_forms):
        
        output = {}
        
        el_pt     = branch_forms["el_pt_NOSYS"]
        el_eta    = branch_forms["el_eta"]
        el_phi    = branch_forms["el_phi"]
        el_mass   = branch_forms["el_m"]
        el_charge = branch_forms["el_charge"]
        content = {"pt": el_pt, "eta": el_eta, "phi": el_phi, "mass": el_mass, "charge": el_charge}
        output["Electron"] = zip_forms(content, "Electron", 'PtEtaPhiMLorentzVector')        
        
        return output
        
    @property
    def behavior(self):
        behavior = {}
        behavior.update(base.behavior)
        behavior.update(vector.behavior)
        return behavior