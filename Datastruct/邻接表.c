#include <stdio.h>
#include <stdlib.h>
/*
需要两个节点：
边表
顶点表
*/

#define MAXVEX 100
typedef char VertexType;
typedef int EdgeType;
typedef int Boolean;

typedef struct EdgeNode{
    int adjvex;//在顶点表中的位置
    struct EdgeNode *next; //下一个节点的内存地址
    EdgeType weight;
}EdgeNode;

typedef struct VertexNode{
    VertexType data;
    struct EdgeNode *firstNode;
}VertexNode,AdjList[MAXVEX];

// 邻接表结构
typedef struct {
    AdjList adjList;
    int numVex,numEdge;
}GraphAdjlist;

// 建立图

void CreateALGraph(GraphAdjlist *G){
    int i,j,k;
    int w;
    EdgeNode *e = NULL;
    printf("请输入边顶点的数量和边的数量:\n");
    scanf("%d,%d",&G->numVex,&G->numEdge);
    // 建立顶点信息
    for(i=0;i<G->numVex;i++){
        printf("输入第一个顶点:");
        scanf("%d",&G->adjList[i].data);
        G->adjList[i].firstNode=NULL; //设置为空
    }
    putchar('\n');
    for(k=0;k<G->numEdge;k++){
        printf("输入边的两个顶点以及权值:(vi,vj,w):\n");
        scanf("%d,%d,%d",&i,&j,&w);
        e = (EdgeNode*)malloc(sizeof(EdgeNode));//e本来就是内存地址
        // 用头插法插入新的节点，尾插还要遍历现在存在的边表
        e->next = G->adjList[i].firstNode;
        G->adjList[i].firstNode = e;
        e->adjvex = j;
        e->weight = w;
    }
    printf("\nDone\n");
}

//图的遍历
/*深度优先搜索DFS*/
Boolean visited[MAXVEX];

void DFS(GraphAdjlist G,int i){
    int j;
    visited[i] = 1;
    printf("我到了%d\n",G.adjList[i].data); //然后遍历这第i行，所有存在链接的顶点
    /*
    // 到达这个节点之后，我要遍历这个顶点后面链接的节点，只能用链表遍历
    j<G.numVex本来就是错的，因为G.numVex是整个图中边的数量，不是这个节点屁股后面的数量
    for(j=0;j<G.numVex;j++){
        if(G.adjList[i].firstNode != NULL && visited[j] != 1){
            DFS(G,j);
        }
    }
    */
    EdgeNode *p = NULL;
    p = G.adjList[i].firstNode;
    while (p!=NULL){
        if(visited[p->adjvex] != 1){
            DFS(G,p->adjvex);
        }
        p = p->next;
    }
}

void DFSTraver(GraphAdjlist G){
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
    GraphAdjlist G;
    CreateALGraph(&G);
    DFSTraver(G);

}



