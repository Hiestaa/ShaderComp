vec4 color9_362;
varying vec4 color7_362;
float w2_362;
float output5_362;
float result6_362;
float z1_362;
float result4_362;
float result3_362;
varying vec3 normal0_362;
vec4 color8_362;
void main(void) {
	color8_362 = vec4(0.5, 1.0, 1.0, 1.0);

	color9_362 =  color8_362 * vec4(1.0, 1.0, 0.5, 1.0);


	float intensity10_362;
	vec4 color7_362;
	vec3 n = normalize(normal0_362);
	
	intensity10_362 = dot(vec3(gl_LightSource[0].position),n);
	
	if (intensity10_362 > 0.95)
		color7_362 = vec4(color9_362.x,color9_362.y,color9_362.z,1.0);
	else if (intensity10_362 > 0.5)
		color7_362 = vec4(color9_362.x / 2.0,color9_362.y / 2.0,color9_362.z / 2.0,1.0);
	else if (intensity10_362 > 0.25)
		color7_362 = vec4(color9_362.x / 4.0,color9_362.y / 4.0,color9_362.z / 4.0,1.0);
	else
		color7_362 = vec4(color9_362.x / 8.0,color9_362.y / 8.0,color9_362.z / 8.0,1.0);


	z1_362 = gl_FragCoord.z;
	w2_362 = gl_FragCoord.w;


	result3_362 = z1_362 / w2_362;


	result4_362 = result3_362 / 25.0;


	output5_362 = log(result4_362);


	result6_362 = clamp(output5_362, 0.0, 1.0);


	gl_FragColor = mix(color7_362, gl_Fog.color, result6_362);

}
