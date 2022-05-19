#ifndef __LIST_H__
#define __LIST_H__

typedef struct cell_t{
  struct cell_t* next;
  float data;
}cell;

void resetTimer();
float getTimer();
int listDelete(struct cell_t* p, int pos);              // リストの要素を削除
int listAdd(struct cell_t* p, float data);              // リストに要素を追加
int listInsert(struct cell_t *p, int pos, float data);  // リストに要素を挿入
int listReplace(struct cell_t *p, int pos, float data); // リストの要素を置き換える
int listLength(struct cell_t *p);                       // リストの長さを取得
float listItem(struct cell_t *p, int pos);              // リストの要素を取得
bool listIsContain(struct cell_t *p, float data);       // リストにデータが含まれるかどうかの確認

#endif
