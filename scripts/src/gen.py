from onshape_robotics_toolkit.connect import Client
from onshape_robotics_toolkit.formats.urdf import URDFSerializer
from onshape_robotics_toolkit.graph import KinematicGraph
from onshape_robotics_toolkit.parse import CAD
from onshape_robotics_toolkit.robot import Robot
from onshape_robotics_toolkit.utilities import setup_default_logging

DOCUMENT_URL = "https://cad.onshape.com/documents/4e1da054bd6bab42d7e2992d/w/8d22cbc1fd08160802a236e9/e/39b03eb076f8268e112e3e99"

setup_default_logging(file_path="quadruped.log", console_level="INFO")

client = Client(env="key.env")
cad = CAD.from_url(DOCUMENT_URL, client=client, max_depth=0)
graph = KinematicGraph.from_cad(cad, use_user_defined_root=True)
robot = Robot.from_graph(kinematic_graph=graph, client=client, name="nogi_beta")

URDFSerializer().save(robot, "nogi_urdf/nogi_beta.urdf", download_assets=True, mesh_dir="nogi_urdf/meshes")
