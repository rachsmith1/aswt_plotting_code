from coffea.nanoevents.schemas.base import BaseSchema, zip_forms
from coffea.nanoevents.methods import base, vector

class ZpeakSchema(BaseSchema):
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
    
class DiphotonSchema(BaseSchema):
    def __init__(self, base_form):
        super().__init__(base_form)
        self._form["contents"] = self._build_collections(self._form["contents"])
        
    def _build_collections(self, branch_forms):
        
        output = {}
        
        ph_pt     = branch_forms["ph_pt_NOSYS"]
        ph_eta    = branch_forms["ph_eta"]
        ph_phi    = branch_forms["ph_phi"]
        ph_mass   = branch_forms["ph_m"]
        content = {"pt": ph_pt, "eta": ph_eta, "phi": ph_phi, "mass": ph_mass}
        output["Photon"] = zip_forms(content, "Photon", 'PtEtaPhiMLorentzVector')   
        
        #output["el_eta"] = branch_forms["el_eta"]
        #output["mu_eta"] = branch_forms["mu_eta"]
        
        return output
        
    @property
    def behavior(self):
        behavior = {}
        behavior.update(base.behavior)
        behavior.update(vector.behavior)
        return behavior
    
class NtupleSchema(BaseSchema):
    def __init__(self, base_form):
        super().__init__(base_form)
        self._form["contents"] = self._build_collections(self._form["contents"])

    def _build_collections(self, branch_forms):

        output = {}
        objects = {
            "Electron": {
                'shortname': "el" ,
                'vars': [ 'pt' , 'eta' , 'phi' , 'charge' , 'select_loose' , 'mass' ] , 
            } ,
            "Muon": {
                'shortname': "mu" ,
                'vars': [ 'pt' , 'eta' , 'phi' , 'charge' , 'select_medium' , 'select_tight' , 'mass' ] ,
            } ,
            "Jet": {
                'shortname': "jet" ,
                'vars': [ 'pt' , 'eta' , 'phi' , 'mass' ] ,
            } ,
            "MET": {
                'shortname': "met" ,
                'vars': [ 'sumet' , 'name' ] ,
            }
        }

        for (obj,objname) in zip(objects.items(),objects):
            objname = obj[1]["shortname"]
            content = {}
            for var in obj[1]['vars']:
                branchname = f'{objname}_{var}'
                if( var in ['pt','sumet','name','select_tight','select_medium','select_loose'] ):
                    branchname = f'{branchname}_NOSYS'
                elif( var == 'mass' ): branchname = branchname.replace( 'mass' , 'm' )
                content[var] = branch_forms[branchname]
            output[obj[0]] = zip_forms(content, obj[0], 'PtEtaPhiMLorentzVector')
        
        output['trigPassed'] = zip_forms({
            k[len('trigPassed')+1:]: branch_forms[k] 
            for k in branch_forms 
            if k.startswith('trigPassed_')
        }, 'trigPassed')
        output["weight"] = branch_forms["generatorWeight_NOSYS"]

        return output

    @property
    def behavior(self):
        behavior = {}
        behavior.update(base.behavior)
        behavior.update(vector.behavior)
        return behavior
    
class NtupleSchemaData(BaseSchema):
    def __init__(self, base_form):
        super().__init__(base_form)
        self._form["contents"] = self._build_collections(self._form["contents"])

    def _build_collections(self, branch_forms):

        output = {}
        objects = {
            "Electron": {
                'shortname': "el" ,
                'vars': [ 'pt' , 'eta' , 'phi' , 'charge' , 'select_loose' , 'mass' ] , 
            } ,
            "Muon": {
                'shortname': "mu" ,
                'vars': [ 'pt' , 'eta' , 'phi' , 'charge' , 'select_medium' , 'select_tight' , 'mass' ] ,
            } ,
            "Jet": {
                'shortname': "jet" ,
                'vars': [ 'pt' , 'eta' , 'phi' , 'mass' ] ,
            } ,
            "MET": {
                'shortname': "met" ,
                'vars': [ 'sumet' , 'name' ] ,
            }
        }

        for (obj,objname) in zip(objects.items(),objects):
            objname = obj[1]["shortname"]
            content = {}
            for var in obj[1]['vars']:
                branchname = f'{objname}_{var}'
                if( var in ['pt','sumet','name','select_tight','select_medium','select_loose'] ):
                    branchname = f'{branchname}_NOSYS'
                elif( var == 'mass' ): branchname = branchname.replace( 'mass' , 'm' )
                content[var] = branch_forms[branchname]
            output[obj[0]] = zip_forms(content, obj[0], 'PtEtaPhiMLorentzVector')

        return output

    @property
    def behavior(self):
        behavior = {}
        behavior.update(base.behavior)
        behavior.update(vector.behavior)
        return behavior
