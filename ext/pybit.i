%module pybitext
%{
#include "pybit.h"
%}

%include <std_vector.i>

std::vector<unsigned char> bits_from_float(float a);
std::vector<unsigned char> bits_from_float_add(float a, float b);
