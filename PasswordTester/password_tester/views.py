from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .serializers import PasswordSerializer
import re

class PasswordTesterView(APIView):
    def get(self, request):
        return render(request, 'password_tester/index.html')
    
    def post(self, request):
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['password']
            strength, feedback = self.check_password_strength(password)
            
            return Response({
                'strength': strength,
                'feedback': feedback
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def check_password_strength(self, password):
        # Initialize score
        score = 0
        feedback = []
        
        # Check length
        if len(password) < 8:
            feedback.append("Password is too short (minimum 8 characters)")
        elif len(password) >= 12:
            score += 2
            feedback.append("Good password length")
        else:
            score += 1
        
        # Check for lowercase letters
        if re.search(r'[a-z]', password):
            score += 1
        else:
            feedback.append("Add lowercase letters")
        
        # Check for uppercase letters
        if re.search(r'[A-Z]', password):
            score += 1
        else:
            feedback.append("Add uppercase letters")
        
        # Check for numbers
        if re.search(r'\d', password):
            score += 1
        else:
            feedback.append("Add numbers")
        
        # Check for special characters
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 1
        else:
            feedback.append("Add special characters")
        
        # Determine strength based on score
        if score < 3:
            strength = "Weak"
            if not feedback:
                feedback.append("Password is too weak")
        elif score < 5:
            strength = "Average"
            if not feedback:
                feedback.append("Password could be stronger")
        else:
            strength = "Strong"
            if not feedback:
                feedback.append("Password is strong")
        
        return strength, ", ".join(feedback)

def home(request):
    return render(request, 'password_tester/index.html')