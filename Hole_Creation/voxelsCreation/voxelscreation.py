#import the H3D fields and types
from H3DInterface import *

# get the reference to the group to put the spheres in
group, = references.getValue()

# create the sphere geometry
#box = createNode( "Box" )
#sizeb = Vec3f( 0.1, 0.1, 0.1 )
#box.size.setValue( sizeb )
#box = ["a", "b"]
#dnn = ["a", "b"]
#for i in range(2):
#	box[i], dnn[i] = createX3DNodeFromString("""<Box DEF="BOX%d" size='0.1 0.1 0.1' solid='true' />""" %(i))

# The AddSphere class adds a new sphere to the group nodes children
# field each time a field routed to it generates an 1 event.
class AddVox( AutoUpdate( SFBool ) ):
  def update( self, event ):
    if( event.getValue() ):
	  for i in range(2):
		t, dn = createX3DNodeFromString( """\
		<Transform>
			<Group DEF="MYGROUP%d">
			<Shape DEF="MYBOX%d">
				<Appearance>
					<Material DEF="MATERIAL%d" diffuseColor='0 0 1' />
						<FrictionalSurface dynamicFriction="0.6" staticFriction="0.6"/>
				</Appearance>
				<Box DEF="BOX%d" size='0.1 0.1 0.1' solid='true' />
			</Shape>

			<PythonScript DEF="PS%d" url="boxerase%d.py" />
	
			<ROUTE fromNode="BOX%d" fromField="isTouched" 
				   toNode="PS%d" toField="eraseme" />
			<ROUTE fromNode="BOX%d" fromField="force" 
				   toNode="PS%d" toField="eraseme" />		 
			<ROUTE fromNode="PS%d" fromField="eraseme" 
				   toNode="MATERIAL%d" toField="diffuseColor" />
				   
			</Group>
		</Transform>""" %(i,i,i,i,i,i,i,i,i,i,i,i) )

		c = RGB( 0, 0, 1 )
		dn["MATERIAL%d" %(i)].diffuseColor.setValue( c )
		#dn["MYBOX%d" %(i)].geometry.setValue( box[i] )
		t.translation.setValue( Vec3f( 0.1,
                                     0.1,
                                     0.1*i ) )
		group.children.push_back( t )
    return event.getValue()

# create an instance of the AddSphere class
add_vox = AddVox()
