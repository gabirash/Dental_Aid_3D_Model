#import the H3D fields and types
from H3DInterface import *
import math

class EraseMe( TypedField( SFVec3f, (MFBool, MFVec3f)  ) ): # PeriodicUpdate to make the update function run periodically regardless of whether you route an instance of this field anywhere. You could chose AutoUpdate if you want instead.
  def update( self, event ):
    group_node = getNamedNode("MYGROUP")
    shape_node = getNamedNode("MYBOX")
    routes_in = self.getRoutesIn()
    is_touched=routes_in[0].getValue()
    ret_force=routes_in[1].getValue()
    if True in is_touched:
      forcex=ret_force[0].x
      forcey=ret_force[0].y
      forcez=ret_force[0].z
      forcetot=math.sqrt(math.pow(forcex,2)+math.pow(forcey,2)+math.pow(forcez,2))
      print(is_touched, ret_force, forcetot)
      if (forcetot>1):
        group_node.children.erase( shape_node )
        print("Erased!")
        return Vec3f(0, 0, 0)
      else:  
        return Vec3f(0, 0, 0)
    else:
      return Vec3f(0, 0, 0)

eraseme = EraseMe()
