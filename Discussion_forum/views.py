from django.views.generic import View
from django.shortcuts import render,redirect
from django.forms.models import modelform_factory
from django.http import HttpResponse
from .models import * 
from .forms import * 
# Create your views here.

def home(request):
    forums=forum.objects.all()
    users=user.objects.all()
    generalcount=forum.objects.filter(category=1).count()
    roomcount=forum.objects.filter(category=50).count()
    tutoringcount=forum.objects.filter(category=3).count()
    codingcount=forum.objects.filter(category=41).count()
    interncount=forum.objects.filter(category=49).count()
    context={'forums':forums,
            'users':users,
            'generalcount':generalcount,
            'roomcount':roomcount,
            'codingcount':codingcount,
            'tutoringcount':tutoringcount,
            'interncount':interncount}
    return render(request,'home.html', context)

def ClassDiscussions(request):
    return render(request, "ClassDiscussions.html")
    
def CodingHelp(request):
    forums=forum.objects.all()
    Ccount=forum.objects.filter(category=42).count()
    CSharpcount=forum.objects.filter(category=43).count()
    Javacount=forum.objects.filter(category=44).count()
    JScount=forum.objects.filter(category=45).count()
    Pythoncount=forum.objects.filter(category=46).count()
    Swiftcount=forum.objects.filter(category=47).count()
    FEcount=forum.objects.filter(category=48).count()
    OLcount=forum.objects.filter(category=58).count()
    context={'forums':forums,
            'Ccount':Ccount,
            'CSharpcount':CSharpcount,
            'Javacount':Javacount,
            'JScount':JScount,
            'Pythoncount':Pythoncount,
            'Swiftcount':Swiftcount,
            'FEcount':FEcount,
            'OLcount':OLcount}
    return render(request, "CodingHelp.html", context)

def Careers(request):
    forums=forum.objects.all()
    appcount=forum.objects.filter(category=51).count()
    webcount=forum.objects.filter(category=52).count()
    MaLcount=forum.objects.filter(category=53).count()
    ArtIcount=forum.objects.filter(category=54).count()
    datacount=forum.objects.filter(category=55).count()
    gamecount=forum.objects.filter(category=56).count()
    infocount=forum.objects.filter(category=57).count()
    OCcount=forum.objects.filter(category=59).count()
    context={'forums':forums,
            'appcount':appcount,
            'webcount':webcount,
            'MaLcount':MaLcount,
            'ArtIcount':ArtIcount,
            'datacount':datacount,
            'gamecount':gamecount,
            'infocount':infocount,
            'OCcount':OCcount,}
    return render(request, "Careers.html", context)

def Core(request):
    forums=forum.objects.all()
    ICScount=forum.objects.filter(category=2).count()
    CS1Acount=forum.objects.filter(category=4).count()
    CS1Bcount=forum.objects.filter(category=5).count()
    CS2count=forum.objects.filter(category=6).count()
    CS3count=forum.objects.filter(category=7).count()
    DScount=forum.objects.filter(category=8).count()
    OScount=forum.objects.filter(category=9).count()
    COcount=forum.objects.filter(category=10).count()
    SEcount=forum.objects.filter(category=11).count()
    CCNcount=forum.objects.filter(category=12).count()
    IDDcount=forum.objects.filter(category=13).count()
    SPLcount=forum.objects.filter(category=14).count()
    ALGOcount=forum.objects.filter(category=15).count()
    CPcount=forum.objects.filter(category=16).count()
    context={'forums':forums,
            'ICScount':ICScount,
            'CS1Acount':CS1Acount,
            'CS1Bcount':CS1Bcount,
            'CS2count':CS2count,
            'CS3count':CS3count,
            'DScount':DScount,
            'OScount':OScount,
            'COcount':COcount,
            'SEcount':SEcount,
            'CCNcount':CCNcount,
            'IDDcount':IDDcount,
            'SPLcount':SPLcount,
            'ALGOcount':ALGOcount,
            'CPcount':CPcount,}
    return render(request,'coreclass.html', context)

def Electives(request):
    forums=forum.objects.all()
    AIcount=forum.objects.filter(category=17).count()
    SPcount=forum.objects.filter(category=18).count()
    BDcount=forum.objects.filter(category=19).count()
    MLcount=forum.objects.filter(category=20).count()
    CAcount=forum.objects.filter(category=21).count()
    DFcount=forum.objects.filter(category=22).count()
    ICcount=forum.objects.filter(category=23).count()
    ILcount=forum.objects.filter(category=24).count()
    ICScount=forum.objects.filter(category=25).count()
    DMcount=forum.objects.filter(category=26).count()
    GDPcount=forum.objects.filter(category=27).count()
    CGcount=forum.objects.filter(category=28).count()
    IScount=forum.objects.filter(category=29).count()
    NLPcount=forum.objects.filter(category=30).count()
    IOScount=forum.objects.filter(category=31).count()
    GECcount=forum.objects.filter(category=32).count()
    WPIcount=forum.objects.filter(category=33).count()
    WPIIcount=forum.objects.filter(category=34).count()
    ADDcount=forum.objects.filter(category=35).count()
    GESNAcount=forum.objects.filter(category=36).count()
    IEcount=forum.objects.filter(category=37).count()
    CNScount=forum.objects.filter(category=38).count()
    HICcount=forum.objects.filter(category=39).count()
    SREcount=forum.objects.filter(category=40).count()
    context={'forums':forums,
            'AIcount':AIcount,
            'SPcount':SPcount,
            'BDcount':BDcount,
            'MLcount':MLcount,
            'CAcount':CAcount,
            'DFcount':DFcount,
            'ICcount':ICcount,
            'ILcount':ILcount,
            'ICScount':ICScount,
            'DMcount':DMcount,
            'GDPcount':GDPcount,
            'CGcount':CGcount,
            'IScount':IScount,
            'NLPcount':NLPcount,
            'IOScount':IOScount,
            'GECcount':GECcount,
            'WPIcount':WPIcount,
            'WPIIcount':WPIIcount,
            'ADDcount':ADDcount,
            'GESNAcount':GESNAcount,
            'IEcount':IEcount,
            'CNScount':CNScount,
            'HICcount':HICcount,
            'SREcount':SREcount}
    return render(request,'electives.html', context)

def addInForum(request):
    if request.user.is_authenticated:
        form = CreateInForum()
        if request.method == 'POST':
            form = CreateInForum(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context ={'form':form}
        return render(request,'addInForum.html',context)
    else: return render(request, 'NotLoggedIn.html')

def addInDiscussion(request):
    if request.user.is_authenticated:
        form = CreateInDiscussion()
        if request.method == 'POST':
            form = CreateInDiscussion(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context ={'form':form}
        return render(request,'addInDiscussion.html',context)
    else: return render(request, 'NotLoggedIn.html')

def GeneralDiscussions(request):
    forums=forum.objects.filter(category="1").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def IntroToCS(request):
    forums=forum.objects.filter(category="2").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def ComputerScience1A(request):
    forums=forum.objects.filter(category="4").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def ComputerScience1B(request):
    forums=forum.objects.filter(category="5").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def ComputerScience2(request):
    forums=forum.objects.filter(category="6").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def ComputerScience3(request):
    forums=forum.objects.filter(category="7").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def DiscreteStructures(request):
    forums=forum.objects.filter(category="8").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def OperatingSystems(request):
    forums=forum.objects.filter(category="9").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def ComputerOrganization(request):
    forums=forum.objects.filter(category="10").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def SoftwareEngineering(request):
    forums=forum.objects.filter(category="11").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def ComputerCommunicationNetworks(request):
    forums=forum.objects.filter(category="12").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def IntroductionToDatabaseDesign(request):
    forums=forum.objects.filter(category="13").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def StructureOfProgrammingLanguages(request):
    forums=forum.objects.filter(category="14").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def DesignAndAnalysisOfAlgorithms(request):
    forums=forum.objects.filter(category="15").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def CapstoneProject(request):
    forums=forum.objects.filter(category="16").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def ArtificialIntelligence(request):
    forums=forum.objects.filter(category="17").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def SystemsProgramming(request):
    forums=forum.objects.filter(category="18").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def BigDataAnalytics(request):
    forums=forum.objects.filter(category="19").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def MachineLearningAndDeepLearning(request):
    forums=forum.objects.filter(category="20").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def CPUArchitectures(request):
    forums=forum.objects.filter(category="21").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def DigitalForensics(request):
    forums=forum.objects.filter(category="22").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def IntroductionToCryptology(request):
    forums=forum.objects.filter(category="23").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def IntermediateLogic(request):
    forums=forum.objects.filter(category="24").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def InternshipInComputerScience(request):
    forums=forum.objects.filter(category="25").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def DataMiningTechniques(request):
    forums=forum.objects.filter(category="26").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def GameDevelopmentPracticum(request):
    forums=forum.objects.filter(category="27").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def ComputerGraphics(request):
    forums=forum.objects.filter(category="28").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def InformationSecurity(request):
    forums=forum.objects.filter(category="29").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def NaturalLanguageProcessing(request):
    forums=forum.objects.filter(category="30").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def iOSProgramming(request):
    forums=forum.objects.filter(category="31").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def GameEngineConcepts(request):
    forums=forum.objects.filter(category="32").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def WebProgrammingI(request):
    forums=forum.objects.filter(category="33").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def WebProgrammingII(request):
    forums=forum.objects.filter(category="34").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def AdvancedDigitalDesign(request):
    forums=forum.objects.filter(category="35").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def GraphAndSocialNetworkAnalysis(request):
    forums=forum.objects.filter(category="36").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def InternetEngineering(request):
    forums=forum.objects.filter(category="37").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def ComputerNetworkSecurity(request):
    forums=forum.objects.filter(category="38").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def HumanInterfaceComputing(request):
    forums=forum.objects.filter(category="39").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def SoftwareRequirementsEngineering(request):
    forums=forum.objects.filter(category="40").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def CPP(request):
    forums=forum.objects.filter(category="42").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def CSharp(request):
    forums=forum.objects.filter(category="43").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def Java(request):
    forums=forum.objects.filter(category="44").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def Javascript(request):
    forums=forum.objects.filter(category="45").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def Python(request):
    forums=forum.objects.filter(category="46").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def Swift(request):
    forums=forum.objects.filter(category="47").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def FrontEnd(request):
    forums=forum.objects.filter(category="48").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def OtherLanguages(request):
    forums=forum.objects.filter(category="58").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def Internships(request):
    forums=forum.objects.filter(category="49").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def TutoringDiscussions(request):
    forums=forum.objects.filter(category="3").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())
    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def Roommate(request):
    forums=forum.objects.filter(category="50").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def ApplicationDevelopment(request):
    forums=forum.objects.filter(category="51").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def WebDevelopment(request):
    forums=forum.objects.filter(category="52").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def MachineLearning(request):
    forums=forum.objects.filter(category="53").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def ArtificialIntel(request):
    forums=forum.objects.filter(category="54").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def DataScience(request):
    forums=forum.objects.filter(category="55").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def GameDevelopment(request):
    forums=forum.objects.filter(category="56").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def InformationTechnology(request):
    forums=forum.objects.filter(category="57").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def OtherCareers(request):
    forums=forum.objects.filter(category="59").order_by('-id')
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'Forums.html', context)

def delete(request, pk):
    forums=forum.objects.get(pk=pk)
    forums.delete()
    return HttpResponse("Forum deleted successfully.")

def deletereply(request, pk):
    print(pk)
    reply=Discussion.objects.get(pk=pk)
    reply.delete()
    return HttpResponse("Reply deleted successfully.")