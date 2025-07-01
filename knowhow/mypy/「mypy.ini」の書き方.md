
#### 設定ファイル名
- mypy.ini
- project.toml

#### ファイル内の記述
###### mypy.ini

    [mypy]
    ...

    コメントなどで日本語が使用できない
    真偽値は、True / False

    モジュール毎の設定は、

    [mypy-<module>.*]
    ignore_errors = True
    のように書く

###### project.toml
    [tool.mypy]
    ...

    コメントなどで日本語が使用でくる
    真偽値は、 true / false
    文字列は、""でくくる

    モジュール毎の設定は、

    [[tool.mypy.overrides]]
    module = "tests.*"
    disallow_untyped_defs = false

    [[tool.mypy.overrides]]
    module = "legacy_code.*"
    ignore_errors = true

    のように書く


#### その他

    mypy がVersion1.17以上のときは、
    mypy --show-config
    で設定値を確認できる


#### 設定値

##### 基本設定
python_version = 3.11
Python 3.11 をターゲットに型チェックを行う。使用している Python のバージョンに合わせる必要があります。

cache_dir = NUL
キャッシュを無効にする設定。Windows の NUL は「何もしない」デバイスなので、キャッシュを保存しません（通常は .mypy_cache に保存されます）。


##### 厳格モード
strict = True
以下のような複数の厳格なチェックオプションを一括で有効にします（ただし、個別に上書き可能）：
disallow_untyped_defs
disallow_incomplete_defs
check_untyped_defs
disallow_untyped_calls
disallow_untyped_decorators
no_implicit_optional
warn_return_any
warn_unused_ignores

##### 型の厳格性に関する設定
check_untyped_defs = true
型アノテーションがない関数の中身もチェック対象にする。

disallow_any_decorated = False
型が Any になるようなデコレーターの使用を許可する。

disallow_any_explicit = False
明示的に Any を使うことを許可する。

disallow_any_expr = False
式中で Any 型が使われることを許可する。

disallow_any_generics = False
ジェネリクス（例：List）で Any を使うことを許可する。

disallow_subclassing_any = True
Any を継承するクラスの定義を禁止する。

##### 関数定義に関する設定
disallow_untyped_calls = True
型が付いていない関数を呼び出すことを禁止する。

disallow_untyped_defs = True
型アノテーションのない関数定義を禁止する。

disallow_incomplete_defs = True
引数の一部にしか型が付いていない関数定義も禁止する。

disallow_untyped_decorators = True
型が付いていないデコレーターの使用を禁止する。

##### その他の厳格性設定
no_implicit_optional = True
デフォルト引数が None の場合でも、明示的に Optional[...] を使うことを要求する。

strict_equality = True
== や != の使用に対して、型が適切かどうかを厳しくチェックする。

##### 警告に関する設定
warn_unused_ignores = True
\# type: ignore が不要な場合に警告を出す。

warn_return_any = True
関数の戻り値が Any 型になる場合に警告を出す。

warn_unreachable = True
到達不能なコードに対して警告を出す。

warn_redundant_casts = True
不要な cast() の使用に対して警告を出す。

warn_no_return = True
戻り値が必要な関数で return 文がない場合に警告を出す。
