#include <Arduino.h>
#include "list.h"

unsigned long startTime;  // For timer

float getTimer() {
  return ((millis() - startTime) / 1000.0);
}

void resetTimer() {
  startTime = millis();
}

// --------------------------------------------
// 概要    : リストからの削除処理
// 引数    : struct _cell_t *p  リストのポインタ
//         : int pos            リストから削除する位置
// 戻り値  : 成功：0, エラー：-1
// --------------------------------------------
int listDelete(struct cell_t* p, int pos)
{
  // 削除位置が0以下の場合、エラーを返す(何もしない)
  if (pos <= 0) { return (-1); }
  // 削除位置がリストの長さよりも大きい場合、エラーを返す(何もしない)
  int l = listLength(p);        // リスト長を取得
  if (l < pos) { return (-1); } 

  cell_t *target, *before;      // 削除する要素とその前の要素
  target = p->next;             // 先頭の次の要素を設定
  before = NULL;
  if (target == NULL) return (-1);  // 既に削除する要素がない場合、エラーを返す
  // 削除対象となる要素に移動する
  before = p;
  for (int i = 0;i < pos-1;i++) {
    if (target->next == NULL) return (-1);  // 削除対象となる要素がない場合、エラーを返す
    before = target;        // 削除対象となる要素の一つ前の要素を退避
    target = target->next;  // 削除対象となる要素の更新
  }
  // 削除対象となる要素が存在する場合
  before->next = target->next;  // 対象の一つ前の要素に対象の次の要素を設定
  delete target;  // 対象を削除
  return(0);
}

// --------------------------------------------
// 概要    : リストへの追加処理
// 引数    : struct _cell_t *p  リストのポインタ
//         : int    data        追加データ
// 戻り値  : 成功：0, エラー：-1
// --------------------------------------------
int listAdd(struct cell_t* p, float data)
{
  cell_t *elm, *last;
  // リスト要素の確保
  elm = new cell_t;
  // 要素の確保に失敗した場合
  if(elm == NULL) {
    // エラーを返す
    return(-1);
  }
  // lastにリストの終端を設定
  last = p;
  for (;;) {
    if (last->next == NULL) break;
    last = last->next;
  }
  // リストの終端に追加する要素の設定
  elm->data = data;
  elm->next = NULL;
  last->next = elm;
  return(0);
}

// --------------------------------------------
// 概要    : リスト長の取得
// 引数    : struct _cell_t *p  リストのポインタ
// 戻り値  : リスト長
// --------------------------------------------
int listLength(struct cell_t* p)
{
  struct cell_t *last;
  // リストの終端に移動
  last = p;
  int length = 0;
  for (;;) {
    if (last->next == NULL) break;
    last = last->next;
    length++;
  }
  // リストの終端に追加する要素の設定
  return(length);
}

// --------------------------------------------
// 概要    : リスト要素の取得
// 引数    : struct _cell_t *p  リストのポインタ
//         : int    pos         リスト要素の取得位置
// 戻り値  : リスト要素、要素が存在しない場合は、0を返す
// --------------------------------------------
float listItem(struct cell_t *p, int pos)
{
  // 取得位置が0以下の場合、0を返す
  if (pos <= 0) { return (0); }
  // 取得位置がリストの長さよりも大きい場合、0を返す
  int l = listLength(p);    // リスト長を取得
  if (l < pos) { return (0); }

  struct cell_t *target;    // 取得する要素
  target = p;               // 先頭の要素を設定
  // 取得対象となる要素に移動する
  for (int i = 0;i < pos;i++) {
    target = target->next;  // 取得対象となる要素の更新
  }
  return target->data;
}

// --------------------------------------------
// 概要    : リストへの挿入処理
// 引数    : struct _cell_t *p   リストのポインタ
//         : int pos             挿入する位置
//         : float data          挿入するデータ
// 戻り値  : 成功：0, エラー：-1
// --------------------------------------------
int listInsert(struct cell_t *p, int pos, float data)
{
  // 挿入位置が0以下の場合、エラーを返す(何もしない)
  if (pos <= 0) { return (-1); }
  // 挿入位置がリストの長さ+1よりも大きい場合、エラーを返す(何もしない)
  int l = listLength(p);  // リスト長を取得
  if (l+1 < pos) { return (-1); } 
  // 挿入位置がリストの終端の場合
  if (l+1 == pos) {
    // リストの終端に追加する
    listAdd(p, data);
    return (0);
  }

  struct cell_t *item, *target, *before;  // 挿入する要素、挿入する位置の要素とその前の要素
  // リスト要素の確保
  item = new cell_t;
  // 要素の確保に失敗した場合、エラーを返す(何もしない)
  if(item == NULL) { return(-1); }

  target = p;
  // 挿入対象となる要素に移動する
  for (int i = 0;i < pos;i++) {
    before = target;        // 挿入対象となる要素の一つ前の要素を退避
    target = target->next;  // 挿入対象となる要素の更新
  }
  // 挿入対象となる要素が存在する場合
  item->data = data;    // 要素のデータの設定
  item->next = target;  // 次の要素を設定
  before->next = item;  // 1つ前の要素に対象の次の要素を設定
  return(0);
}

// --------------------------------------------
// 概要    : リストの要素の置換処理
// 引数    : struct _cell_t *p  リストのポインタ
//         : int pos            置換する位置
//         : float data         置換するデータ
// 戻り値  : 成功：0, エラー：-1
// --------------------------------------------
int listReplace(struct cell_t *p, int pos, float data)
{
  // 置換位置が0以下の場合、エラーを返す(何もしない)
  if (pos <= 0) { return (-1); }
  // 置換位置がリストの長さよりも大きい場合、エラーを返す(何もしない)
  int l = listLength(p);  // リスト長を取得
  if (l < pos) { return (-1); } 

  struct cell_t *target;  // 置換する要素

  target = p;
  // 置換対象となる要素に移動する
  for (int i = 0;i < pos;i++) {
    target = target->next;  // 置換対象となる要素の更新
  }
  // 置換対象となる要素が存在する場合
  target->data = data;      // 要素のデータの設定
  return(0);
}

// --------------------------------------------
// 概要    : リストの要素に指定データが存在するか？
// 引数    : struct _cell_t *p  リストのポインタ
//         : float data         検索するデータ
// 戻り値  : 存在する：true, 存在しない：false
// --------------------------------------------
bool listIsContain(struct cell_t *p, float data)
{
  struct cell_t *elm = p;
  // リストの全要素に対してdataを検索する
  for (;;) {
    // リスト終端に到達したらbreak
    if (elm->next == NULL) break;
    // リストの次の要素を取得
    elm = elm->next;
    // リストにdataが存在する場合、trueを返す
    if (elm->data == data) return true;
  }
  // リストにdataが存在しない場合、falseを返す
  return false;
}


