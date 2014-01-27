varying vec3 normal0_362;
void main(void) {

	normal0_362 = gl_NormalMatrix * gl_Normal;


	gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;

}
