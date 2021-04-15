"""DataFlair_discsnForum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from Discussion_forum.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('addInForum/',addInForum,name='addInForum'),
    path('addInDiscussion/',addInDiscussion,name='addInDiscussion'),
    path('GeneralDiscussions/', GeneralDiscussions,name="GeneralDiscussions"),
    path('ClassDiscussions/', ClassDiscussions,name="ClassDiscussions"),
    path('ClassDiscussions/Core/', Core, name="Core"),
    path('ClassDiscussions/Core/IntroToCS', IntroToCS,name="IntroToCS"),
    path('ClassDiscussions/Core/ComputerScience1A', ComputerScience1A,name="CS1A"),
    path('ClassDiscussions/Core/ComputerScience1B', ComputerScience1B,name="CS1B"),
    path('ClassDiscussions/Core/ComputerScience2', ComputerScience2,name="CS2"),
    path('ClassDiscussions/Core/ComputerScience3', ComputerScience3,name="CS3"),
    path('ClassDiscussions/Core/DiscreteStructures', DiscreteStructures,name="DiscreteStructures"),
    path('ClassDiscussions/Core/OperatingSystems', OperatingSystems,name="OperatingSystems"),
    path('ClassDiscussions/Core/ComputerOrganization', ComputerOrganization,name="ComputerOrganization"),
    path('ClassDiscussions/Core/SoftwareEngineering', SoftwareEngineering,name="SoftwareEngineering"),
    path('ClassDiscussions/Core/ComputerCommunicationNetworks', ComputerCommunicationNetworks,name='ComputerCommunicationNetworks'),
    path('ClassDiscussions/Core/IntroductionToDatabaseDesign',IntroductionToDatabaseDesign,name='IntroductionToDatabaseDesign'),
    path('ClassDiscussions/Core/StructureOfProgrammingLanguages', StructureOfProgrammingLanguages, name='StructureOfProgrammingLanguages'),
    path('ClassDiscussions/Core/DesignAndAnalysisOfAlgorithms', DesignAndAnalysisOfAlgorithms, name='DesignAndAnalysisOfAlgorithms'),
    path('ClassDiscussions/Core/CapstoneProject', CapstoneProject, name="CapstoneProject"),
    path('ClassDiscussions/Electives/', Electives, name="Electives"),
    path('ClassDiscussions/Electives/ArtificialIntelligence', ArtificialIntelligence, name="ArtificialIntelligence"),
    path('ClassDiscussions/Electives/SystemsProgramming', SystemsProgramming, name="SystemsProgramming"),
    path('ClassDiscussions/Electives/BigDataAnalytics', BigDataAnalytics, name="BigDataAnalytics"),
    path('ClassDiscussions/Electives/MachineLearningAndDeepLearning', MachineLearningAndDeepLearning, name="MachineLearningAndDeepLearning"),
    path('ClassDiscussions/Electives/CPUArchitectures', CPUArchitectures, name="CPUArchitectures"),
    path('ClassDiscussions/Electives/DigitalForensics', DigitalForensics, name="DigitalForensics"),
    path('ClassDiscussions/Electives/IntroductionToCryptology', IntroductionToCryptology, name='IntroductionToCryptology'),
    path('ClassDiscussions/Electives/IntermediateLogic', IntermediateLogic, name="IntermediateLogic"),
    path('ClassDiscussions/Electives/InternshipInComputerScience', InternshipInComputerScience, name="InternshipInComputerScience"),
    path('ClassDiscussions/Electives/DataMiningTechniques', DataMiningTechniques, name="DataMiningTechniques"),
    path('ClassDiscussions/Electives/GameDevelopmentPracticum', GameDevelopmentPracticum, name="GameDevelopmentPracticum"),
    path('ClassDiscussions/Electives/ComputerGraphics', ComputerGraphics, name="ComputerGraphics"),
    path('ClassDiscussions/Electives/InformationSecurity', InformationSecurity, name="InformationSecurity"),
    path('ClassDiscussions/Electives/NaturalLanguageProcessing', NaturalLanguageProcessing, name="NaturalLanguageProcessing"),
    path('ClassDiscussions/Electives/iOSProgramming', iOSProgramming, name="iOSProgramming"),
    path('ClassDiscussions/Electives/GameEngineConcepts', GameEngineConcepts, name="GameEngineConcepts"),
    path('ClassDiscussions/Electives/WebProgrammingI', WebProgrammingI, name="WebProgrammingI"),
    path('ClassDiscussions/Electives/WebProgrammingII', WebProgrammingII, name="WebProgrammingII"),
    path('ClassDiscussions/Electives/AdvancedDigitalDesign', AdvancedDigitalDesign, name="AdvancedDigitalDesign"),
    path('ClassDiscussions/Electives/GraphAndSocialNetworkAnalysis', GraphAndSocialNetworkAnalysis, name='GraphAndSocialNetworkAnalysis'),
    path('ClassDiscussions/Electives/InternetEngineering', InternetEngineering, name="InternetEngineering"),
    path('ClassDiscussions/Electives/ComputerNetworkSecurity', ComputerNetworkSecurity, name='ComputerNetworkSecurity'),
    path('ClassDiscussions/Electives/HumanInterfaceComputing', HumanInterfaceComputing, name='HumanInterfaceComputing'),
    path('ClassDiscussions/Electives/SoftwareRequirementsEngineering', SoftwareRequirementsEngineering, name='SoftwareRequirementsEngineering'),
    path('CodingHelp/', CodingHelp, name="CodingHelp"),
    path('CodingHelp/C++', CPP, name="CPP"),
    path('CodingHelp/CSharp', CSharp, name="CSharp"),
    path('CodingHelp/Java', Java, name="Java"),
    path('CodingHelp/Javascript', Javascript, name="Javascript"),
    path('CodingHelp/Python', Python, name="Python"),
    path('CodingHelp/Swift', Swift, name="Swift"),
    path('CodingHelp/FrontEnd', FrontEnd, name="FrontEnd"),
    path('CodingHelp/OtherLanguages', OtherLanguages, name="OtherLanguages"),
    path('TutoringDiscussions/', TutoringDiscussions,name="TutoringDiscussions"),
    path('Internships/', Internships, name='Internships'),
    path('Careers/', Careers, name="Careers"),
    path('Careers/ApplicationDevelopment/', ApplicationDevelopment, name="ApplicationDevelopment"),
    path('Careers/WebDevelopment/', WebDevelopment, name="WebDevelopment"),
    path('Careers/MachineLearning/', MachineLearning, name='MachineLearning'),
    path('Careers/ArtificialIntelligence/', ArtificialIntel, name="ArtificialIntel"),
    path('Careers/DataScience/', DataScience, name="DataScience"),
    path('Careers/GameDevelopment/', GameDevelopment, name="GameDevelopment"),
    path('Careers/InformationTechnology/', InformationTechnology, name="InformationTechnology"),
    path('Careers/OtherCareers', OtherCareers, name="OtherCareers"),
    path('Roommate/', Roommate, name="Roommate"),
    path('deleteforum/<int:pk>', delete, name="deleteforum"),
    path('deletereply/<int:pk>', deletereply, name="deletereply")
]

handler404 = 'Discussion_forum.views.error_404'
handler500 = 'Discussion_forum.views.error_500'