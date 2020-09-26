#include <stdio.h>

typedef char VertexType;
typedef int EdgeType; //权值
typedef int Boolean;

#define MAXVEX 100
#define INF 65535

/*
定义邻接矩阵的结构
{
    顶点表：一维数组
    边表：二维矩阵
}
*/

typedef struct{
    VertexType vexs[MAXVEX];
    EdgeType arc[MAXVEX][MAXVEX];
    int numVex,numEdge; //当前图的定点数和边数
}MGraph;

//创建无向图
void CreateMGraph(MGraph *G){
    int i,j;
    int k;
    int w;
    printf("输入顶点数和边数\n");
    scanf("%d,%d",&G->numVex,&G->numEdge);
    printf("开始输入顶点\n");
    for (i=0;i<G->numVex;i++){
        printf("第%d个顶点\n",i+1);
        scanf("%d",&G->vexs[i]);
    }
    printf("\n顶点输入完毕\n");
    printf("初始化边表\n");
    for(i=0;i<G->numVex;i++){
        for(j=0;j<G->numVex;j++){
            G->arc[i][j] = INF;
        }
    }
    printf("初始化完毕\n");
    for(k=0;k<G->numEdge;k++){
        printf("输入(vi,vj)和权值w\n");
        printf("输入第%d条边\n",k+1);
        scanf("%d,%d,%d",&i,&j,&w);
        G->arc[i][j] = w;
        G->arc[j][i] = w; //无向图
    }
    

}

//图的遍历
/*深度优先搜索DFS*/
Boolean visited[MAXVEX];

void DFS(MGraph G,int i){
    int j;
    visited[i] = 1;
    printf("我到了%d",G.vexs[i]); //然后遍历这第i行，所有存在链接的顶点
    for(j=0;j<G.numVex;j++){
        if(G.arc[i][j] == 1 && visited[j] != 1){
            DFS(G,j);
        }
    }
}

void DFSTraver(MGraph G){
    int i = 0;
    for(i=0;i<G.numVex;i++){
        visited[i] = 0; // 初始化所有节点为没有访问的状态
    }
    //开始访问
    for(i=0;i<G.numVex;i++){
        if(visited[i] == 0){
            DFS(G,i);
        }
    }
}

int main()
{
    MGraph G;
    CreateMGraph(&G);
    DFSTraver(G);

}