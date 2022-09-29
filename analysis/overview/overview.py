import matplotlib.pyplot as plt

def make_plot(data, names, xlabel, color):
    fig, ax = plt.subplots()
    
    ax.bar(names, data, color=color)
    ax.set_ylim([0, max(data) + (max(data) * 0.1)])
    ax.set_xlabel(xlabel, fontweight='bold')
    ax.set_ylabel('Github Stars', fontweight='bold')
    
    for index, data in enumerate(data):
        plt.text(x=index , y =data+500 , s=f"{data}" , fontdict=dict(fontsize=12), ha='center')
    
    plt.show()

javascript = [58400, 33100, 43000, 14000]
javascript_names = ['Express','Koa','Meteor', 'Hapi']
make_plot(javascript, javascript_names, 'Javascript (Node.js runtime) frameworks', 'orange')

python = [66600, 49700, 60600]
python_names = ['Django', 'FastAPI', 'Flask'] 
make_plot(python, python_names, 'Python frameworks', 'yellow')

java = [49200, 1200, 2700, 12200]
java_names = ['Sprng', 'Struts', 'Grails', 'Play']
make_plot(java, java_names, 'Java frameworks', 'red')

golang = [63000, 28900, 23800, 23900, 18400]
golang_names = ['Gin', 'Beego', 'Echo', 'Kit', 'Fasthttp']
make_plot(golang, golang_names, 'Golang frameworks', 'blue')
