from H3DInterface import *

# The LinSpring class generates a spring force that tries to keep the
# nodes in the origin.
#
# routes_in[0] is the position of the DynamicTransform node.
class LinSpring( SFVec3f ):
  def __init__( self, constant ):
    SFVec3f.__init__( self )
    self.constant=constant
  def update( self, event ):
    dist = event.getValue()
    return -dist * self.constant

linSpring = LinSpring( 100 )

# The LinDamper class generates a force to dampen the linear motion
# of a DynamicTransform.
#
# routes_in[0] is the velocity of the DynamicTransform node.
class LinDamper( SFVec3f ):
  def __init__( self, constant ):
    SFVec3f.__init__( self )
    self.constant=constant
  def update( self, event ):
    vel = event.getValue()
    return -vel * self.constant

linDamper = LinDamper( 10 )

# The SumForces class just sums all SFVec3f fields that are routed to it.
class SumForces( TypedField( SFVec3f, (SFVec3f, SFVec3f, MFVec3f) ) ):
  def update( self, event ):
    f = Vec3f( 0, 0, 0 );
    routes = self.getRoutesIn()
    for r in routes:
      if isinstance( r, SFVec3f ):
        f = f + r.getValue();
        print(f)
      elif isinstance( r, MFVec3f ):
        forces = r.getValue()
        for force in forces:
          f = f + force
    return f

class InvertForce( TypedField( MFVec3f, (MFVec3f) ) ):
  def update( self, event ):
    try:
      forces, matrix = self.getRoutesIn()
      print(forces)
      if( forces == event ):
        forces = event.getValue()
        forces_to_return = []
        to_global = matrix.getValue().getRotationPart()
        for force in forces:
          forces_to_return.append( ( to_global * force ) * -1 )
        return forces_to_return
      else:
        return [Vec3f( 0, 0, 0 ) ]
    except:
      return [Vec3f(0,0,0)]

sumForces = SumForces()
invertForce = InvertForce()
linSpring.route( sumForces )
linDamper.route( sumForces )
invertForce.route( sumForces )

