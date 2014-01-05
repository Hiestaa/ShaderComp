float result3_4527;
float result2_4527;
float output4_4527;
float result5_4527;
float w1_4527;
float z0_4527;
void main(void) {

	z0_4527 = gl_FragCoord.z;
	w1_4527 = gl_FragCoord.w;


	result2_4527 = z0_4527 / w1_4527;


	result3_4527 = result2_4527 / 25.0;


	output4_4527 = log(result3_4527);


	result5_4527 = clamp(output4_4527, 0.0, 1.0);


	gl_FragColor = mix(vec4(0.5, 0.5, 1.0, 1.0), gl_Fog.color, result5_4527);

}
