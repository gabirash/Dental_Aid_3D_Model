# This is the example from the H3D Manual(Examples section)

#import the H3D fields and types
from H3DInterface import *
import math

class EraseMe( TypedField( SFVec3f, (MFBool, MFVec3f)  ) ): # PeriodicUpdate to make the update function run periodically regardless of whether you route an instance of this field anywhere. You could chose AutoUpdate if you want instead.
  def update( self, event ):
    group_node = getNamedNode("MYGROUP1")
    shape_node = getNamedNode("MYBOX1")
    routes_in = self.getRoutesIn()
    is_touched=routes_in[0].getValue()
    ret_force=routes_in[1].getValue()
    #is_touched = event.getValue()
    print(is_touched, ret_force)
    if True in is_touched:
      forcex=ret_force[0].x
      forcey=ret_force[0].y
      forcez=ret_force[0].z
      forcetot=math.sqrt(math.pow(forcex,2)+math.pow(forcey,2)+math.pow(forcez,2))
      #group_node.children.erase( shape_node )
      print(is_touched, ret_force, forcetot)
      if (forcetot>2.5):
        group_node.children.erase( shape_node )
        print("Erased!")
        return Vec3f(0, 0, 0)
      else:  
        return Vec3f(0, 0, 0)
    else:
      return Vec3f(0, 0, 0)
    #return RGB( 1, 1, 0 ) # Need to return something, since this field at the moment is not routed anywhere just make sure the correct type is returned. The M at the beginning of the field class it inherits from means that a list needs to be returned. In this case I chose an empty list.

eraseme = EraseMe()
