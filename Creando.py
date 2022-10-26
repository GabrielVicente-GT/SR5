from Object import *
import gl
from vector import *
from textures import *

def vertice_transform(vertex, scale, translate):

    return V3(
            (vertex[0] * scale[0]) + translate[0], #X.
            (vertex[1] * scale[1]) + translate[1], #Y.
            (vertex[2] * scale[2]) + translate[2] #Z.
    )

def cargando_modelo():
    renderizado = gl.RenderizadoFuncio()

    # #Bmax
    # scale_factor = (12,12,12)
    # translate_factor = (500, 50,0)
    # cube = Obj(',/Bigmax_White_Obj.obj')


    # # taza
    # scale_factor = (9,9,10)
    # translate_factor = (500, 50,0)
    # cube = Obj('./taza.obj')

    # #Cara Clase
    # scale_factor = (450,450,600)
    # translate_factor = (525, 500,0)
    # cube = Obj('./model.obj')
    # renderizado.texture = Texture('./model.bmp')

    # #Perro
    # scale_factor = (2000,2000,3000)
    # translate_factor = (850, 150,0)
    # cube = Obj('./Perro.obj')
    # renderizado.texture = Texture('./Shiba.bmp')



    # # kakashi
    # scale_factor = (9,9,10)
    # translate_factor = (500, 50,0)
    # cube = Obj('./kakashi.obj')

    # # woman
    # scale_factor = (1,1,1)
    # translate_factor = (500, 500,0)
    # cube = Obj('./woman.obj')

    # # Faraon
    # scale_factor = (125,125,250)
    # translate_factor = (525, 50,0)
    # cube = Obj('./faraon.obj')

    # # Mascara
    # scale_factor = (3000,3000,3000)
    # translate_factor = (7150,50,0)
    # cube = Obj('./Objts/Mask.obj')
    # renderizado.texture = Texture('./Textrs/Mask3.bmp')

    # # Caballo
    # scale_factor = (0.5,0.5,1)
    # translate_factor = (500,600,0)
    # cube = Obj('./Textrs/juan.obj')
    # renderizado.texture = Texture('./Textrs/juan.bmp')
    # gl.EscrituraSobreTextura('./Textrs/madara.obj','./Textrs/madara.bmp')

    # # Pato
    # scale_factor = (15,15,30)
    # translate_factor = (500,400,0)
    # cube = Obj('./Objts/Pato.obj')
    # renderizado.texture = Texture('./Textrs/Pato.bmp')
    # gl.EscrituraSobreTextura('./Objts/Pato.obj','./Textrs/Pato.bmp')

    # Gato
    scale_factor = (15,15,10)
    translate_factor = (500,400,0)
    cube = Obj('./Objts/Gato.obj')
    renderizado.texture = Texture('./Textrs/Gato.bmp')
    gl.EscrituraSobreTextura('./Objts/Gato.obj','./Textrs/Gato.bmp')

    for face in cube.faces:
        f1 = face[0][0] - 1
        f2 = face[1][0] - 1
        f3 = face[2][0] - 1

        v1 = vertice_transform(cube.vertices[f1], scale_factor, translate_factor)
        v2 = vertice_transform(cube.vertices[f2], scale_factor, translate_factor)
        v3 = vertice_transform(cube.vertices[f3], scale_factor, translate_factor)

        if len(face) == 4:

            f4 = face[3][0] - 1
            v4 = vertice_transform(cube.vertices[f4], scale_factor, translate_factor)

            if renderizado.texture:
                ft1 = face[0][1] - 1
                ft2 = face[1][1] - 1
                ft3 = face[2][1] - 1
                ft4 = face[3][1] - 1

                vt1 = V3(*cube.tvertices[ft1])
                vt2 = V3(*cube.tvertices[ft2])
                vt3 = V3(*cube.tvertices[ft3])
                vt4 = V3(*cube.tvertices[ft3])

                gl.triangulo_version_dos_textura((v1,v2,v3),(vt1,vt2,vt3))
                gl.triangulo_version_dos_textura((v1,v3,v4),(vt1,vt3,vt3))
            else:
                gl.triangulo_version_dos_textura((v1,v2,v3))
                gl.triangulo_version_dos_textura((v1,v3,v4))
            # gl.triangulo_version_dos(v1,v2,v3)
            # gl.triangulo_version_dos(v1,v3,v4)

            # gl.glLine3(v1[0][0], v1[0][1], v2[0][0],v2[0][1])
            # gl.glLine3(v2[0][0], v2[0][1], v3[0][0],v3[0][1])
            # gl.glLine3(v3[0][0], v3[0][1], v4[0][0],v4[0][1])
            # gl.glLine3(v4[0][0], v4[0][1], v1[0][0],v1[0][1])


        elif len(face) == 3:
            # gl.triangulo_version_dos(v1,v2,v3)
            # gl.glLine3(v1[0][0], v1[0][1], v2[0][0],v2[0][1])
            # gl.glLine3(v2[0][0], v2[0][1], v3[0][0],v3[0][1])
            # gl.glLine3(v3[0][0], v3[0][1], v1[0][0],v1[0][1])

            if renderizado.texture:
                ft1 = face[0][1] - 1
                ft2 = face[1][1] - 1
                ft3 = face[2][1] - 1

                vt1 = V3(*cube.tvertices[ft1])
                vt2 = V3(*cube.tvertices[ft2])
                vt3 = V3(*cube.tvertices[ft3])
                gl.triangulo_version_dos_textura((v1,v2,v3),(vt1,vt2,vt3))

            else:
                gl.triangulo_version_dos_textura((v1,v2,v3))

