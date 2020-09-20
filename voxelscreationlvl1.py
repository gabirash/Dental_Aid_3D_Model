#import the H3D fields and types
from H3DInterface import *

# get the reference to the group to put the voxels in
group, = references.getValue()

# The AddSphere class adds a new sphere to the group nodes children
class AddVox( AutoUpdate( SFBool ) ):
  def update( self, event ):
    if( event.getValue() ):
		group_node = getNamedNode("MACRO")
		shape_node = getNamedNode("GUIT")
		group_node.children.erase( shape_node )
		for z in range (9):
			for y in range (20):
				for x in range (20):
					if (z >= 0 and z <= 3):
						t, dn = createX3DNodeFromString ("""\
			  									                    <Transform DEF="TR">
			  									                        <Group DEF="MYGROUP%d%d%d">
			  									                        <Shape DEF="MYBOX%d%d%d">
			  									                            <Appearance>
			  									                                <Material DEF="MATERIAL%d%d%d" diffuseColor='1 1 1' />
			  									                                    <FrictionalSurface dynamicFriction="0.3" staticFriction="0.3"/>
			  									                            </Appearance>
			  									                            <Box DEF="BOX%d%d%d" size='0.005 0.005 0.005' solid='true' />
			  									                        </Shape>

			  									                        <PythonScript DEF="PS%d%d%d" url="boxeraseP%d%d%d.py" />

			  									                        <ROUTE fromNode="BOX%d%d%d" fromField="isTouched" 
			  									                            toNode="PS%d%d%d" toField="eraseme" />
			  									                        <ROUTE fromNode="BOX%d%d%d" fromField="force" 
			  									                            toNode="PS%d%d%d" toField="eraseme" />		 
			  									                        <ROUTE fromNode="PS%d%d%d" fromField="eraseme" 
			  									                            toNode="TR" toField="center" />

			  									                        </Group>
			  									                    </Transform>""" % (
							x, y, z, x, y, z, x, y, z, x, y, z, x, y, z, x, y, z, x, y, z, x, y, z, x, y, z, x, y, z, x,
							y,
							z))
						c = RGB (1, 0, 0)
						dn["MATERIAL%d%d%d" % (x, y, z)].diffuseColor.setValue (c)
					elif (z >= 4 and z <= 6):
						t, dn = createX3DNodeFromString ("""\
			  									                    <Transform DEF="TR">
			  									                        <Group DEF="MYGROUP%d%d%d">
			  									                        <Shape DEF="MYBOX%d%d%d">
			  									                            <Appearance>
			  									                                <Material DEF="MATERIAL%d%d%d" diffuseColor='1 1 1' />
			  									                                    <FrictionalSurface dynamicFriction="0.3" staticFriction="0.3"/>
			  									                            </Appearance>
			  									                            <Box DEF="BOX%d%d%d" size='0.005 0.005 0.005' solid='true' />
			  									                        </Shape>

			  									                        <PythonScript DEF="PS%d%d%d" url="boxeraseD%d%d%d.py" />

			  									                        <ROUTE fromNode="BOX%d%d%d" fromField="isTouched" 
			  									                            toNode="PS%d%d%d" toField="eraseme" />
			  									                        <ROUTE fromNode="BOX%d%d%d" fromField="force" 
			  									                            toNode="PS%d%d%d" toField="eraseme" />		 
			  									                        <ROUTE fromNode="PS%d%d%d" fromField="eraseme" 
			  									                            toNode="TR" toField="center" />

			  									                        </Group>
			  									                    </Transform>""" % (
							x, y, z, x, y, z, x, y, z, x, y, z, x, y, z, x, y, z, x, y, z, x, y, z, x, y, z, x, y, z, x,
							y,
							z))
						c = RGB (1, 1, 0)
						dn["MATERIAL%d%d%d" % (x, y, z)].diffuseColor.setValue (c)
					elif (z >= 7 and z <= 8):
						t, dn = createX3DNodeFromString ("""\
			  									                    <Transform DEF="TR">
			  									                        <Group DEF="MYGROUP%d%d%d">
			  									                        <Shape DEF="MYBOX%d%d%d">
			  									                            <Appearance>
			  									                                <Material DEF="MATERIAL%d%d%d" diffuseColor='1 1 1' />
			  									                                    <FrictionalSurface dynamicFriction="0.3" staticFriction="0.3"/>
			  									                            </Appearance>
			  									                            <Box DEF="BOX%d%d%d" size='0.005 0.005 0.005' solid='true' />
			  									                        </Shape>

			  									                        <PythonScript DEF="PS%d%d%d" url="boxeraseE%d%d%d.py" />

			  									                        <ROUTE fromNode="BOX%d%d%d" fromField="isTouched" 
			  									                            toNode="PS%d%d%d" toField="eraseme" />
			  									                        <ROUTE fromNode="BOX%d%d%d" fromField="force" 
			  									                            toNode="PS%d%d%d" toField="eraseme" />		 
			  									                        <ROUTE fromNode="PS%d%d%d" fromField="eraseme" 
			  									                            toNode="TR" toField="center" />

			  									                        </Group>
			  									                    </Transform>""" % (
							x, y, z, x, y, z, x, y, z, x, y, z, x, y, z, x, y, z, x, y, z, x, y, z, x, y, z, x, y, z, x,
							y,
							z))
						if (z == 8 and ((x == 1 and ((y >= 3 and y <= 6) or (y >= 13 and y <= 16)))
										or ((x == 2 or x == 7) and (y == 2 or y == 7 or y == 12 or y == 17))
										or ((x == 3 or x == 4 or x == 5) and (y == 1 or y == 8 or y == 11 or y == 18))
										or (x == 6 and (y == 2 or y == 7 or y == 11 or y == 18))
										or (x == 8 and (y == 3 or y == 6 or (y >= 13 and y <= 16)))
										or ((x == 9 or x == 10 or x == 11) and (y == 3 or y == 6))
										or (x == 12 and (y == 2 or y == 7 or y == 15))
										or (x == 13 and (y == 2 or y == 7 or y == 14 or y == 16))
										or (x == 14 and (y == 1 or y == 8 or y == 12 or y == 13 or y == 17 or y == 18))
										or (x == 15 and (y == 1 or y == 8 or y == 14 or y == 16))
										or (x == 16 and (y == 1 or y == 8 or y == 15))
										or (x == 17 and (y == 2 or y == 7))
										or (x == 18 and (y >= 3 and y <= 6)))):
							c = RGB (0, 0, 0)
							dn["MATERIAL%d%d%d" % (x, y, z)].diffuseColor.setValue (c)
					t.translation.setValue (Vec3f ((0.005 * x - 0.0475 + 0.065),
												   (0.005 * y - 0.0475 + 0.045),
												   (0.005 * z - 0.02)))
					group.children.push_back (t)
    return event.getValue ()

# create an instance of the AddVox class
add_vox = AddVox()
