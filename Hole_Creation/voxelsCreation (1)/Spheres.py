import random

#import the H3D fields and types
from H3DInterface import *

# get the reference to the group to put the spheres in
group, = references.getValue()

# create the sphere geometry
#sphere = createNode( "Sphere" )
#sphere.radius.setValue( 0.02 )

sphere, dnn = createX3DNodeFromString( """<Sphere DEF="SPH0" radius="0.02" />""")

# The AddSphere class adds a new sphere to the group nodes children
# field each time a field routed to it generates an 1 event.
class AddSphere( AutoUpdate( SFBool ) ):
  def update( self, event ):
    if( event.getValue() ):
	  for i in range(5):
		t, dn = createX3DNodeFromString( """\
		<Transform>
		<Group DEF="GRP">
			<Shape DEF="SHAPE" >
				<Appearance>
				<Material DEF="MATERIAL" />
				</Appearance>
			</Shape>
			<PythonScript DEF="PSS" url="Sphere.py" />
			<MouseSensor DEF="MS" />
			<ROUTE fromNode="MS" fromField="rightButton" 
			toNode="PSS" toField="color" />		 
			<ROUTE fromNode="PSS" fromField="color" 
			toNode="MATERIAL" toField="diffuseColor" />
		</Group>
		</Transform>""")

		c = RGB( random.random(), random.random(), random.random() )
		dn["MATERIAL"].diffuseColor.setValue( c )
		dn["SHAPE"].geometry.setValue( sphere )
		t.translation.setValue( Vec3f( c.r * 0.5 - 0.25,
                                     c.g * 0.5 - 0.25,
                                     c.b * 0.5 - 0.25 ) )
		group.children.push_back( t )
    return event.getValue()

# create an instance of the AddSphere class
add_sphere = AddSphere()
